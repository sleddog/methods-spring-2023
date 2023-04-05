from flask import Flask, request

app = Flask(__name__)

@app.route('/can-i-golf')
def can_i_golf():
    city = request.args.get('city')
    state = request.args.get('state')
    # Call OpenWeatherMap API to get weather data for city and state
    # Process the weather data to determine if the user can golf
    can_golf = True
    if can_golf:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
