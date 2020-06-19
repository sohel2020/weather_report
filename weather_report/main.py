import requests
import pytz
import click
import sys
from prettytable import PrettyTable
from datetime import datetime

def date_time_date(timestamp):
  return datetime.fromtimestamp(timestamp, tz= pytz.timezone('Asia/Dhaka')).date()

def date_time_time(timestamp):
  return datetime.fromtimestamp(timestamp, tz= pytz.timezone('Asia/Dhaka')).time()

def kelvin_celsius(kelvin):
  return round((kelvin - 273.15), 2)

@click.command()
@click.option('--days', default=1, type=int, help='Number of days.')
@click.option('--city', required=True, type=str, help='Name of the city.')

def main(city, days):
  BASE_URL= "https://api.openweathermap.org/data/2.5/forecast/daily"
  apikey = "bbe42d1367edac5d11b95ece38dc060d"
  URL = BASE_URL + '?q=' + city + '&cnt=' + str(days) + '&appid=' + apikey

  table = PrettyTable(['date', 'sunrise', 'sunset', 'min_temp', 'max_temp'])
  response = requests.get(url = URL)
  if response.status_code == 404:
    print(f'Invalid city named {city}')
    sys.exit()
    
  for data in response.json().get('list'):
    date = date_time_date(data.get('dt'))
    sunrise = date_time_time(data.get('sunrise'))
    sunset = date_time_time(data.get('sunset'))
    min_temp = kelvin_celsius(data.get('temp').get('min'))
    max_temp = kelvin_celsius(data.get('temp').get('max'))
    table.add_row([date, sunrise, sunset, min_temp, max_temp])

  print(table)


if __name__ == "__main__":
    main()

