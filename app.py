import requests
import os

# https://openweathermap.org/api/one-call-api

# empire state building
lat = '40.75009231913161'
lon = '-73.98638285425646'
exclude = 'minutely,hourly,alerts'

url = 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_key}&units=imperial'


def handler(event, context):
    response = requests.get(url.format(
        lat=lat,
        lon=lon,
        exclude=exclude,
        API_key=os.getenv('WEATHER_API_KEY')
    ))

    data = response.json()

    rain_conditions = ['rain', 'thunderstorm', 'drizzle']
    snow_conditions = ['snow']

    today_weather = data['daily'][0]['weather'][0]['main'].lower()

    if today_weather in rain_conditions:
        print('Pack an umbrella!')
        return 'Pack an umbrella!'
    elif today_weather in snow_conditions:
        print('Pack your snow boots!')
        return 'Pack your snow boots!'
    else:
        print('Clear skies today!')
        return 'Clear skies today!'
