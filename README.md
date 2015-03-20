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
surf to https://developer.forecast.io/ for an api key

use http://dbsgeo.com/latlon/ (or something else) to get coordinates for your location

## options
```
  <no arg>    shows current weather
  -h, --help  shows help message
  -d          daily forecast (max 8 days)
  -ho         hourly forecast (max 24 hours)
  -l L        limit forecast output to <L> entries
```
