# Add a CRUD Rest API for managing user objects
#

# import the flask module
import flask

# import the flask_restful module
import flask_restful

# import the flask_sqlalchemy module
import flask_sqlalchemy

# import the flask_marshmallow module
import flask_marshmallow

# import the marshmallow module
import marshmallow

# import the marshmallow_sqlalchemy module
import marshmallow_sqlalchemy

# import the flask_cors module
import flask_cors

# import the flask_migrate module
import flask_migrate

# import the flask_script module
import flask_script

# import the flask_httpauth module
import flask_httpauth

# import the werkzeug.security module
import werkzeug.security

# import the flask_jwt_extended module
import flask_jwt_extended

# import the flask_jwt module
import flask_jwt

# import the flask_jwt_simple module
import flask_jwt_simple

# import the flask_jwt_extended module
import flask_jwt_extended

def hello():
    print('hello world')

# create a flask app
app = flask.Flask(__name__)

# create a flask_restful api
api = flask_restful.Api(app)

# create a flask_sqlalchemy db
db = flask_sqlalchemy.SQLAlchemy(app)

# create a flask_marshmallow ma
ma = flask_marshmallow.Marshmallow(app)

# create a flask_cors cors
cors = flask_cors.CORS(app)

# create a flask_migrate Migrate
migrate = flask_migrate.Migrate(app, db)

# create a flask_script Manager
manager = flask_script.Manager(app)

# create a flask_httpauth HTTPBasicAuth
auth = flask_httpauth.HTTPBasicAuth()

# create a flask_jwt JWT
jwt = flask_jwt.JWT(app)

# create a flask_jwt_simple JWTManager
jwt = flask_jwt_simple.JWTManager(app)

# create a flask_jwt_extended JWTManager
jwt = flask_jwt_extended.JWTManager(app)



# create a user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



# create a user schema
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "username", "email")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# create a user resource
class UserResource(flask_restful.Resource):
    def get(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return result

    def post(self):
        new_user = User(
            username=flask.request.json['username'],
            email=flask.request.json['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)
    



