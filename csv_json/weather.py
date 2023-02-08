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
disable(CRITICAL)

FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'
CURRENT_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
API_KEY = dotenv_values('.env')['API_KEY']

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'location', help='location to query weather of'
    )
    return parser.parse_args()

def process_responses(res_forecast, res_current_weather):
    debug(loads(res_forecast.text)['list'][0])
    debug(loads(res_forecast.text)['list'][8])
    debug(res_current_weather.text)

    res_forecast = loads(res_forecast.text)
    res_current_weather = loads(res_current_weather.text)
    weather_data = []
    current_weather_data = {
        'main': res_current_weather['weather'][0]['main'],
        'description': res_current_weather['weather'][0]['description']
    }
    weather_data.append(current_weather_data)
    i = 0
    while len(weather_data) < 3:
        weather_data.append({
            'main': res_forecast['list'][i]['weather'][0]['main'],
            'description': res_forecast['list'][i]['weather'][0]['description']
        }) 
        i += 8
    
    debug(weather_data)
    return weather_data

def display_weather(location, weather):
    print('The weather at {} for:'.format(location.title()))

    print('Today:')
    print('\t', weather[0]['main'], '-', weather[0]['description'])

    print('\nTomorrow:')
    print('\t', weather[1]['main'], '-', weather[1]['description'])

    print('\nDay after tomorrow:')
    print('\t', weather[2]['main'], '-', weather[2]['description'])

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

    display_weather(location, weather)


    print('Done')

if __name__ == '__main__':
    main()