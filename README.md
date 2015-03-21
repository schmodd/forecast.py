# forecast.py
weather forecast powered by forecast.io

## requirements
- python3
- requests
- prettytable 

## configuration
you have to enter valid entries for:
```
API_KEY='' 
LAT=''
LONG=''
```
- surf to https://developer.forecast.io/ for an api key
- use http://dbsgeo.com/latlon/ (or something else) to get coordinates for your location

## options
by default (without passing any args) the current weather is shown
```
  usage: forecast.py [-h] [-df | -hf]
  
  -h, --help  shows help message
  -df         daily forecast
  -hf         hourly forecast
```