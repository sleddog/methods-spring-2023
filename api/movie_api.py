# using the movie api pull down a list of all the movies that tom hanks has been in

import requests
import json
import pprint

url = "https://api.themoviedb.org/3/search/person?api_key=1f54bd990f1cdfb230adb312546d765d&language=en-US&query=Tom%20Hanks&page=1&include_adult=false"
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()

movies = data["results"]
print(movies)