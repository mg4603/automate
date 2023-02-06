'''
1) read location as command line arg
2) request open weather api for weather data
3) process json data 
4) print weather for the next three days.
'''
from argparse import ArgumentParser
from json import loads
from logging import debug, disable, basicConfig, DEBUG, CRITICAL
from dotenv import dotenv_values
from requests import get

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'
CURRENT_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
API_KEY = dotenv_values('.env')['API_KEY']

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'location', help='location to query weather of'
    )
    return parser.parse_args()


def main():
    print('Fetching Current Weather Data')
    print()
    print(
        'Fetch current weather data and forecasts for tomorrow and day-after.'
    )
    args = parse_args()
    location = args.location

    debug(API_KEY)    
    res_forecast = get(FORECAST_URL.format(location, API_KEY))
    res_forecast.raise_for_status()

    res_current_weather = get(CURRENT_WEATHER_URL.format(location, API_KEY))
    res_current_weather.raise_for_status()

    weather = process_responses(res_forecast, res_current_weather)

    display_weather(weather)


    print('Done')

if __name__ == '__main__':
    main()