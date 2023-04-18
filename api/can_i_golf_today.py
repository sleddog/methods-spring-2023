from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/can-i-golf')
def can_i_golf():
    city = request.args.get('city')
    state = request.args.get('state')
    if not city or not state:
        return 'Please provide both city and state as URL parameters.', 400

    # Make a request to the OpenWeatherMap API to retrieve the weather information for the given location
    weather_api_key = 'ed14717162c738f7249f12572c878a63'
    # url = f'https://api.openweathermap.org/data/3.0/weather?q={city},{state},US&appid={weather_api_key}&units=imperial'
    # url = f'https://api.openweathermap.org/data/3.0/onecall?lat=47.5053&lon=111.3008&exclude=hourly,daily&appid={weather_api_key}'

    # Great Falls, MT
    lat = 47.5053
    lon = 111.3008


    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=imperial'
    # url = api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=ed14717162c738f7249f12572c878a63 
    print(url)
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code != 200:
        return f'Error retrieving weather information: {response.json().get("message")}', response.status_code

    # Retrieve the temperature and wind speed from the API response
    data = response.json()
    print(data)
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']

    # Determine if golfing is recommended based on the temperature and wind speed
    if temp > 60 and wind_speed < 10:
        return 'Yes, you can go golfing today!'
    else:
        return 'No, it is not recommended to go golfing today due to the weather conditions.'

if __name__ == '__main__':
    app.run(debug=True)