from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ganti dengan API Key dari OpenWeatherMap
API_KEY = '-----'
URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric', 
            }
            response = requests.get(URL, params=params)
            data = response.json()

            if data.get('cod') != 200:
                error_message = data.get('message', 'City not found!')
            else:
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'wind': data['wind']['speed'],
                }

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
