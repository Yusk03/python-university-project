from os import getenv
from requests import get
from dotenv import load_dotenv

load_dotenv()

API_KEY = getenv('OPENWEATHERMAP_API_KEY')
API_CITY_URL = 'https://api.openweathermap.org/geo/1.0/direct'
API_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def get_coordinates_by_city(city: str):
    response = get(f'{API_CITY_URL}?q={city}&appid={API_KEY}')

    if response.status_code == 200:
        try:
            data = response.json()
            return data[0]['lat'], data[0]['lon']
        except ValueError:
            print('Failed to parse JSON response.')
        except IndexError:
            print(f'Ooops index error, probably not exists city {city}')
    else:
        print(f'Failed get coordinates of city {city}. HTTP status code {response.status_code}')

    return 0, 0


def get_weather_forecast(lat: float, lon: float):
    response = get(f'{API_WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}')

    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except ValueError:
            print('Failed to parse JSON response.')
    else:
        print(f'Failed get forecast for this city :(')

    return {}

