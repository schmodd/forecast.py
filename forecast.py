#!/usr/bin/env python
# -*- coding: utf-8 -*-

# todo: add alerts, colors

import requests
import json
import datetime
import argparse
import sys
from prettytable import PrettyTable

# surf to https://developer.forecast.io/ for an api key
# use http://dbsgeo.com/latlon/ to get coordinates for your location
API_KEY=''
LAT=''
LONG=''
LIMIT=24 # limit hourly forecast output (48 max)

#some api settings
UNITS='si' # auto possibly shows wrong measuring unit
LANG='en'

def formatDatetime(unixTime, outputFormat='%d. %b. %H:%M'):
    return datetime.datetime.fromtimestamp(unixTime).strftime(outputFormat)

def getMeasuringUnit():
    return '\N{DEGREE SIGN}F' if UNITS == 'us' else '\N{DEGREE SIGN}C'

def getPrecip(probability, type):
    probability = '{:3.0f} {:1}'.format(probability * 100, '%')
    return '{:} {:>5}'.format(probability, '-') if type == 0 else '{:} {:>5}'.format(probability, type)

def showDaily(measuring_unit):
    HEAD = ['Date', 'Temp min', 'Temp max', 'HUM', 'SR', 'SS', 'Precip', 'Summary']
    table = PrettyTable(HEAD, border = False, padding_width = 2)
    table.align='r'
    table.align['Date'] = 'l'
    table.align['Summary'] = 'l'
    for day in result['daily']['data']:
        table.add_row([formatDatetime(day['time'], '%d. %b.'), '{:4.2f} {:2}'.format(day['temperatureMin'], 
            measuring_unit), '{:4.2f} {:2}'.format(day['temperatureMax'], measuring_unit), 
            '{:3.0f} {:1}'.format(day['humidity'] * 100, '%'), formatDatetime(day['sunriseTime'], '%H:%M'),
            formatDatetime(day['sunsetTime'], '%H:%M'), getPrecip(day['precipProbability'], 
            day['precipType'] if day['precipProbability'] > 0 else 0), day['summary']]) 
    print('\n', end='')
    print(table)

def showHourly(measuring_unit):
    HEAD = ['Date', 'Temp', 'HUM', 'Precip', 'Summary']
    table = PrettyTable(HEAD, border = False, padding_width = 2)
    table.align='r'
    table.align['Date'] = 'l'
    table.align['Summary'] = 'l'
    for hour in result['hourly']['data'][0:LIMIT]:
        table.add_row([formatDatetime(hour['time'], '%d. %b. %H:%M'), '{:4.2f} {:2}'.format(hour['temperature'], 
            measuring_unit), '{:3.0f} {:1}'.format(hour['humidity'] * 100, '%'), getPrecip(hour['precipProbability'],
            hour['precipType'] if hour['precipProbability'] > 0 else 0), hour['summary']])
    print('\n', end='')
    print(table)

if __name__ == '__main__':
    if not API_KEY or not LAT or not LONG:
        sys.exit("aborted! please make sure api-key and coordinates are specified")
    
    parser = argparse.ArgumentParser(description='weather forecast powered by forecast.io')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-df', help='daily forecast', action='store_true')
    group.add_argument('-hf', help='hourly forecast', action='store_true')
    args = parser.parse_args()

    BASE_URL = 'https://api.forecast.io/forecast/'
    SETTINGS = API_KEY + '/' + LAT + ',' + LONG + '?units=' + UNITS + '&lang='+ LANG + '&exclude=flags,minutely,'
    URL = BASE_URL + SETTINGS
    HTTP_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
        'Accept-Encoding': 'gzip'}
    MEAS_UNIT = getMeasuringUnit()

    if args.df:
        URL += 'hourly,currently'
    elif args.hf:
        URL += 'daily,currently'
    else:
        URL += 'hourly,daily'

    result = requests.get(URL, headers=HTTP_HEADERS)

    if result.status_code == 200:
        result = result.json()

        if args.df:
            showDaily(MEAS_UNIT)
        elif args.hf:
            showHourly(MEAS_UNIT)
        else:
            print('{:} {:10}'.format('\n date:', formatDatetime(result['currently']['time'])), end='')
            print('{:} {:6.2f} {:2}'.format(' | temp:', result['currently']['temperature'], MEAS_UNIT), end='')
            print('{:} {:2.0f} {:1}'.format(' | humidity:', result['currently']['humidity'] * 100, '%'), end='')
            print('{:} {:}'.format(' | precipitation:', getPrecip(result['currently']['precipProbability'], 
                result['currently']['precipType'] if result['currently']['precipProbability'] > 0 else 0)))
    else:
        print('aborted! problems connecting to forecast.io')
