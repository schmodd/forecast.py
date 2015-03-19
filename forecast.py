#!/usr/bin/env python
# -*- coding: utf-8 -*-

# todo: add alerts, colors

import requests
import json
import datetime
import argparse
import sys

# surf to https://developer.forecast.io/ for an api key
# use http://dbsgeo.com/latlon/ to get coordinates for your location
API_KEY=''
LAT=''
LONG=''
#some api settings
UNITS='si' # auto possibly shows wrong measuring unit
LANG='de'

def formatDatetime(unixTime, outputFormat='%d %b %H:%M'):
    return datetime.datetime.fromtimestamp(unixTime).strftime(outputFormat)

def getMeasuringUnit():
    return '°F' if UNITS == 'us' else '°C'

def showDaily(limit):
    print('\n{0:6}    {1:}    {2:}    {3:}'.format('Date', 'Min ' + getMeasuringUnit(), 'Max ' + 
        getMeasuringUnit(), 'Summary'))
    for day in result['daily']['data'][0:limit]:
        print('{0:6}    {1:>6.2f}    {2:>6.2f}    {3:50}'.format(formatDatetime(day['time'], '%d %b'), 
            day['temperatureMin'], day['temperatureMax'], day['summary']))

def showHourly(limit):
    print('\n{0:6}    {1:}    {2:}    {3:}'.format('Date', 'Time', 'Temp ' + getMeasuringUnit(), 'Summary'))
    for hour in result['hourly']['data'][0:limit]:
        print('{0:6}    {1:5}    {2:>6.2f}    {3:50}'.format(formatDatetime(hour['time'], '%d %b'),
            formatDatetime(hour['time'], '%H:%M'), hour['temperature'], hour['summary']))

if __name__ == '__main__':

    # setup args
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

    if args.d:
        URL += 'hourly,currently'
        result = requests.get(URL, headers=HTTP_HEADERS).json()
        showDaily(args.l)
    elif args.ho:
        URL += 'daily,currently'
        result = requests.get(URL, headers=HTTP_HEADERS).json()
        showHourly(args.l)
    else:
        URL += 'hourly,daily'
        result = requests.get(URL, headers=HTTP_HEADERS).json()
        print('\ntime: '+ formatDatetime(result['currently']['time']) + ' | temp: ' + 
            str(result['currently']['temperature']) + ' ' + getMeasuringUnit() + ' | humidity: ' + 
            str(result['currently']['humidity']*100) + ' %')
