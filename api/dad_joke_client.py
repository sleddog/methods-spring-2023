# write a python client that calls https://icanhazdadjoke.com/ and prints out a random dad joke
# use the requests library to make the request
# use the json library to parse the response
# use the pprint library to print the response
# use the argparse library to add a command line argument to specify the number of jokes to print


import requests
import json
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num_jokes", help="number of jokes to print", type=int)
args = parser.parse_args()

url = "https://icanhazdadjoke.com/search"
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()

jokes = data["results"]
for joke in jokes:
    print(joke["joke"])
