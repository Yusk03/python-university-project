from src.api.open_weather_map import get_coordinates_by_city, get_weather_forecast

def weather_info(city: str, date: str):
    lat, lon = get_coordinates_by_city(city or 'Івано-Франківськ')

    if not lat or not lon:
        print(f'Oops, lat {lat} or lon {lon} not valid. Please check your city name or enter in English name')
        return 0

    data = get_weather_forecast(lat, lon)

    if not data or not data['list']:
        print(f'Not valid result from open weather server. Please check API key')
        return 0

    for forecast in data['list']:
        if date not in forecast['dt_txt']:
            continue

        forecast_date = forecast['dt_txt']
        weather = forecast['weather'][0]['description']
        temperature = forecast['main']['temp']
        humidity = forecast['main']['humidity']
        wind_speed = forecast['wind']['speed']

        forecast_result = (
            f"\nWeather forecast for at {forecast_date}:\n"
            f"  - Weather: {weather}\n"
            f"  - Temperature: {temperature}K\n"
            f"  - Humidity: {humidity}%\n"
            f"  - Wind Speed: {wind_speed}m/s\n\n"
        )

        print(forecast_result)

    return 1
