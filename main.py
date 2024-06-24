from src.utils.console_menu import menu
from src.utils.date_range import date_range_list
from src.weather import weather_info


def main():
    print('Welcome to simple forecast project')
    city = input('Enter the city name: [Івано-Франківськ]: ')

    dates = date_range_list()

    (_, date) = menu({
        'options': dates,
        'message': 'Select date (Forecast limited to 5 day):',
    })

    print(f'Selected date {date}')

    print(f'Fetching weather data for {city}...')
    weather_info(city, date)


if __name__ == '__main__':
    main()
