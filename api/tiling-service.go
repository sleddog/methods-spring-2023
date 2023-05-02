// A go service exposing a graphql endpoint for a dynamic tiling service connected to Postgres with the PostGIS extension.  
// It will create mapping tiles directly from a SQL query.  It will also cache tiles in Redis.

package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/go-redis/redis"
	"github.com/gorilla/handlers"
	"github.com/gorilla/mux"
	"github.com/graphql-go/graphql"
	"github.com/graphql-go/handler"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

var (
	// Version is the version of the service
	Version = "0.0.0"
	// Build is the build number of the service
	Build = "0"
	// BuildTime is the time the service was built
	BuildTime = "0"
)

var (
	// DB is the database connection
	DB *sqlx.DB
	// Redis is the redis connection
	Redis *redis.Client
	// Schema is the graphql schema
	Schema graphql.Schema
)


func main() {
	// Parse command line flags
	var (
		port     = flag.Int("port", 8080, "The port to listen on")
		dbURL    = flag.String("db-url", "", "The database connection string")
		redisURL = flag.String("redis-url", "", "The redis connection string")
	)
	flag.Parse()

	// Connect to the database
	var err error
	DB, err = sqlx.Connect("postgres", *dbURL)
	if err != nil {
		log.Fatal(err)
	}

	// Connect to redis
	Redis = redis.NewClient(&redis.Options{
		Addr: *redisURL,
	})

	// Create the graphql schema
	Schema, err = graphql.NewSchema(graphql.SchemaConfig{
		Query: graphql.NewObject(graphql.ObjectConfig{
			Name: "Query",
			Fields: graphql.Fields{
				"tile": &graphql.Field{
					Type:        TileType,
					Description: "Get a tile",
					Args: graphql.FieldConfigArgument{
						"z": &graphql.ArgumentConfig{
							Type: graphql.NewNonNull(graphql.Int),
						},
						"x": &graphql.ArgumentConfig{
							Type: graphql.NewNonNull(graphql.Int),
						},
						"y": &graphql.ArgumentConfig{
							Type: graphql.NewNonNull(graphql.Int),
						},
						"query": &graphql.ArgumentConfig{
							Type: graphql.NewNonNull(graphql.String),
						},
					},
					Resolve: func(p graphql.ResolveParams) (interface{}, error) {
						z := p.Args["z"].(int)
						x := p.Args["x"].(int)
						y := p.Args["y"].(int)
						query := p.Args["query"].(string)

						return GetTile(z, x, y, query)
					}
				},
			},
		}),
	})
	if err != nil {
		log.Fatal(err)
	}
	
	// Create the graphql handler
	h := handler.New(&handler.Config{
		Schema:   &Schema,
		Pretty:   true,
		GraphiQL: true,
	})

	// Create the router
	r := mux.NewRouter()
	r.Handle("/graphql", h)
	r.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	})
	r.HandleFunc("/version", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(fmt.Sprintf("Version: %s Build: %s Build Time: %s", Version, Build, BuildTime)))
	})

	// Create the server
	s := &http.Server{
		Addr:           fmt.Sprintf(":%d", *port),
		Handler:        handlers.LoggingHandler(os.Stdout, r),
		ReadTimeout:    10 * time.Second,
		WriteTimeout:   10 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}		

	// Start the server
	log.Printf("Starting server on port %d", *port)
	log.Fatal(s.ListenAndServe())
}


// GetTile returns a tile
func GetTile(z, x, y int, query string) (*Tile, error) {
	// Get the tile from redis
	tile, err := getTileFromRedis(z, x, y)
	if err != nil {
		return nil, err
	}

	// If the tile is not in redis, get it from the database
	if tile == nil {
		tile, err = getTileFromDB(z, x, y, query)
		if err != nil {
			return nil, err
		}
	}

	return tile, nil

}

// getTileFromRedis returns a tile from redis
func getTileFromRedis(z, x, y int) (*Tile, error) {
	// Get the tile from redis
	key := fmt.Sprintf("tile:%d:%d:%d", z, x, y)
	val, err := Redis.Get(key).Result()
	if err != nil {
		if err == redis.Nil {
			return nil, nil
		}
		return nil, err
	}

	// Parse the tile
	tile, err := parseTile(val)
	if err != nil {
		return nil, err
	}

	return tile, nil
}

// getTileFromDB returns a tile from the database
func getTileFromDB(z, x, y int, query string) (*Tile, error) {
	// Get the tile from the database
	var tile *Tile
	err := DB.Get(&tile, query, z, x, y)
	if err != nil {
		return nil, err
	}

	// Save the tile in redis
	err = saveTileInRedis(z, x, y, tile)
	if err != nil {
		return nil, err
	}

	return tile, nil
}

// saveTileInRedis saves a tile in redis
func saveTileInRedis(z, x, y int, tile *Tile) error {
	// Save the tile in redis
	key := fmt.Sprintf("tile:%d:%d:%d", z, x, y)
	val, err := tile.String()
	if err != nil {
		return err
	}
	_, err = Redis.Set(key, val, 0).Result()
	if err != nil {
		return err
	}

	return nil
}


// Tile is a tile
type Tile struct {
	Features []Feature `json:"features"`
}

// Feature is a feature
type Feature struct {
	Type       string                 `json:"type"`
	Properties map[string]interface{} `json:"properties"`
	Geometry   Geometry               `json:"geometry"`
}

// Geometry is a geometry
type Geometry struct {
	Type        string    `json:"type"`
	Coordinates []float64 `json:"coordinates"`
}

// String returns the string representation of a tile
func (t *Tile) String() (string, error) {
	b, err := json.Marshal(t)
	if err != nil {
		return "", err
	}

	return string(b), nil
}

// parseTile parses a tile
func parseTile(s string) (*Tile, error) {
	var t *Tile
	err := json.Unmarshal([]byte(s), &t)
	if err != nil {
		return nil, err
	}

	return t, nil
}

// TileType is the graphql type for a tile
var TileType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Tile",
	Fields: graphql.Fields{
		"features": &graphql.Field{
			Type: graphql.NewList(FeatureType),
		},
	},
})

// FeatureType is the graphql type for a feature
var FeatureType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Feature",
	Fields: graphql.Fields{
		"type": &graphql.Field{
			Type: graphql.String,
		},
		"properties": &graphql.Field{
			Type: graphql.NewList(PropertyType),
		},
		"geometry": &graphql.Field{
			Type: GeometryType,
		},
	},
})

// PropertyType is the graphql type for a property
var PropertyType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Property",
	Fields: graphql.Fields{
		"key": &graphql.Field{
			Type: graphql.String,
		},
		"value": &graphql.Field{
			Type: graphql.String,
		},
	},
})

// GeometryType is the graphql type for a geometry
var GeometryType = graphql.NewObject(graphql.ObjectConfig{
	Name: "Geometry",
	Fields: graphql.Fields{
		"type": &graphql.Field{
			Type: graphql.String,
		},
		"coordinates": &graphql.Field{
			Type: graphql.NewList(graphql.Float),
		},
	},
})

// TileArgs are the arguments for the tile query
var TileArgs = graphql.FieldConfigArgument{
	"z": &graphql.ArgumentConfig{
		Type: graphql.Int,
	},
	"x": &graphql.ArgumentConfig{
		Type: graphql.Int,
	},
	"y": &graphql.ArgumentConfig{
		Type: graphql.Int,
	},
}

// TileResolver is the resolver for the tile query
var TileResolver = func(p graphql.ResolveParams) (interface{}, error) {
	// Get the arguments
	z := p.Args["z"].(int)
	x := p.Args["x"].(int)
	y := p.Args["y"].(int)

	// Get the tile
	tile, err := GetTile(z, x, y, TileQuery)
	if err != nil {
		return nil, err
	}

	return tile, nil
}

// TileQuery is the query to get a tile
var TileQuery = `
	SELECT
		jsonb_build_object(
			'type', 'FeatureCollection',