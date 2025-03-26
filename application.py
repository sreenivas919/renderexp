from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "50eb5f7a07cc66cf3b8ea6b59b154c84"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None
    if request.method == 'POST':
        city = request.form.get('city').strip()
        if city:
            params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = 'City not found. Please try again.'
    return render_template('index.html', weather=weather_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
