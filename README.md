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
#### default
```
$ forecast.py

  date: 27. Mar. 12:28 | temp:  11.48 °C | humidity: 72 % | precipitation:   0 %     -
```

#### daily forecast
```
$ forecast.py -df

  Date        Temp min    Temp max      HUM       SR       SS         Precip    Summary
  27. Mar.     5.25 °C    12.26 °C     83 %    05:54    18:31     98 %  rain    Light rain starting in the afternoon, continuing until evening.
  28. Mar.     3.74 °C    11.32 °C     78 %    05:52    18:33     10 %  rain    Light rain overnight.
  29. Mar.     7.84 °C    13.83 °C     86 %    06:49    19:34     99 %  rain    Light rain in the morning and afternoon and breezy starting in the evening.
  30. Mar.     5.09 °C    10.79 °C     77 %    06:47    19:36    100 %  rain    Light rain until afternoon and breezy until evening.
  31. Mar.     5.24 °C    10.12 °C     83 %    06:44    19:38    100 %  rain    Light rain until evening and breezy throughout the day.
  01. Apr.     4.34 °C     7.74 °C     75 %    06:42    19:40     85 %  rain    Light rain and breezy until evening.
  02. Apr.     3.19 °C     7.72 °C     74 %    06:40    19:41     92 %  rain    Breezy until afternoon and light rain starting in the afternoon, continuing until evening.
  03. Apr.     1.21 °C     8.76 °C     77 %    06:37    19:43     62 %  rain    Breezy until afternoon and drizzle starting in the evening.
```

#### hourly forecast
```
$ forecast.py -hf

  Date                  Temp      HUM         Precip    Summary
  27. Mar. 12:00     9.73 °C     69 %      0 %     -    Mostly Cloudy
  27. Mar. 13:00    10.67 °C     69 %      0 %     -    Mostly Cloudy
  27. Mar. 14:00    11.39 °C     68 %     12 %  rain    Drizzle
  27. Mar. 15:00    11.70 °C     67 %     43 %  rain    Light Rain
  27. Mar. 16:00    11.59 °C     67 %     55 %  rain    Light Rain
  27. Mar. 17:00    11.06 °C     71 %     49 %  rain    Light Rain
  27. Mar. 18:00    10.48 °C     79 %     20 %  rain    Drizzle
  27. Mar. 19:00     9.76 °C     85 %      2 %  rain    Mostly Cloudy
  27. Mar. 20:00     9.10 °C     88 %      0 %     -    Mostly Cloudy
  27. Mar. 21:00     8.54 °C     89 %      0 %     -    Partly Cloudy
  27. Mar. 22:00     8.18 °C     90 %      0 %     -    Partly Cloudy
  27. Mar. 23:00     7.56 °C     92 %      0 %     -    Partly Cloudy
  28. Mar. 00:00     6.88 °C     94 %      0 %     -    Clear
  28. Mar. 01:00     6.27 °C     95 %      0 %     -    Clear
  28. Mar. 02:00     5.67 °C     95 %      0 %     -    Clear
  28. Mar. 03:00     5.09 °C     95 %      0 %     -    Clear
  28. Mar. 04:00     4.61 °C     95 %      0 %     -    Partly Cloudy
  28. Mar. 05:00     4.18 °C     95 %      0 %     -    Partly Cloudy
  28. Mar. 06:00     3.74 °C     94 %      0 %     -    Mostly Cloudy
  28. Mar. 07:00     4.03 °C     91 %      0 %     -    Mostly Cloudy
  28. Mar. 08:00     5.16 °C     86 %      0 %     -    Mostly Cloudy
  28. Mar. 09:00     6.80 °C     78 %      0 %     -    Mostly Cloudy
  28. Mar. 10:00     8.30 °C     71 %      0 %     -    Partly Cloudy
  28. Mar. 11:00     9.46 °C     65 %      0 %     -    Partly Cloudy
```
