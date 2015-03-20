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
#some api settings
UNITS='si' # auto possibly shows wrong measuring unit
LANG='en'

def formatDatetime(unixTime, outputFormat='%d. %b. %H:%M'):
    return datetime.datetime.fromtimestamp(unixTime).strftime(outputFormat)

def getMeasuringUnit():
    return '°F' if UNITS == 'us' else '°C'

def showDaily(limit, measuring_unit):
    HEAD = ['Date', 'Temp min', 'Temp max', 'Humidity', 'Summary']
    table = PrettyTable(HEAD, border = False, padding_width = 2)
    table.align='r'
    table.align['Date'] = 'l'
    table.align['Summary'] = 'l'
    for day in result['daily']['data'][0:limit]:
        table.add_row([formatDatetime(day['time'], '%d. %b.'), '{:6.2f} {:2}'.format(day['temperatureMin'], 
            measuring_unit), '{:6.2f} {:2}'.format(day['temperatureMax'], measuring_unit), 
            '{:2.0f} {:1}'.format(day['humidity']*100, '%'), day['summary']]) 
    print('\n', end='')
    print(table)

def showHourly(limit, measuring_unit):
    HEAD = ['DateTime', 'Temp', 'Humidity', 'Summary']
    table = PrettyTable(HEAD, border = False, padding_width = 2)
    table.align='r'
    table.align['DateTime'] = 'l'
    table.align['Summary'] = 'l'
    for hour in result['hourly']['data'][0:limit]:
        table.add_row([formatDatetime(hour['time'], '%d. %b. %H:%M'), '{:6.2f} {:2}'.format(hour['temperature'], 
            measuring_unit), '{:2.0f} {:1}'.format(hour['humidity']*100, '%'), hour['summary']])
    print('\n', end='')
    print(table)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='weather forecast powered by forecast.io')
    parser.add_argument('-d', help='daily forecast', action='store_true')
    parser.add_argument('-ho', help='hourly forecast', action='store_true')
    parser.add_argument('-l', help='limit forecast output to x hours/days', 
        type=int, default=24)
    args = parser.parse_args()

    BASE_URL = 'https://api.forecast.io/forecast/'
    SETTINGS = API_KEY + '/' + LAT + ',' + LONG + '?units=' + UNITS + '&lang='+ LANG + '&exclude=flags,minutely,'
    URL = BASE_URL + SETTINGS
    HTTP_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
        'Accept-Encoding': 'gzip'}
    MEAS_UNIT = getMeasuringUnit()

    if args.d:
        URL += 'hourly,currently'
    elif args.ho:
        URL += 'daily,currently'
    else:
        URL += 'hourly,daily'

    result = requests.get(URL, headers=HTTP_HEADERS).json()

    if args.d:
        print(URL)
        showDaily(args.l, MEAS_UNIT)
    elif args.ho:
        showHourly(args.l, MEAS_UNIT)
    else:
        print('{:} {:10}'.format('\n time:', formatDatetime(result['currently']['time'])), end='')
        print('{:} {:6.2f} {:2}'.format(' | temp:', result['currently']['temperature'], MEAS_UNIT), end='')
        print('{:} {:2.0f} {:1}'.format(' | humidity:', result['currently']['humidity']*100, '%'))
