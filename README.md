# forecast.py
weather forecast powered by forecast.io

## requirements
- python3
- requests
- prettytable 

## setup
you have to setup a few things (in the script) before running:
```
API_KEY='' 
LAT=''
LONG=''
```
- surf to https://developer.forecast.io/ for an api key
- use http://dbsgeo.com/latlon/ (or something else) to get coordinates for your location

## execution
by default (without passing any args) the current weather is shown
```
  usage: forecast.py [-h] [-df | -hf]
  
  -h, --help  shows help message
  -df         daily forecast
  -hf         hourly forecast
```
