# forecast.py
cli weather forecast powered by forecast.io

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
by default (without passing any args) the current weather is shown, see modes for detailed explanation
```
  usage: forecast.py [-h] [-df | -hf]
  
  -h, --help  shows help message
  -df         daily forecast
  -hf         hourly forecast
```

## modes
### default
- shows date, temperature, humidity, precipitation
#### daily forecast
- shows date, temperature, humidity, precipitation, summary
#### hourly forecast
- shows date, temperature minimum, temperature maximum, humidity, sunrise, sunset, precipitation, summary

## what it looks like
click to watch at original size

![preview](what_it_looks_like.png?raw=true)
