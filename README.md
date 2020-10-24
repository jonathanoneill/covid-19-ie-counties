# COVID-19 - Ireland County Data

## Data

This example used the **Covid19CountyStatisticsHPSCIreland** dataset from https://covid-19.geohive.ie/

## Use

```
$ python3 covid-ie-counties.py --help
usage: covid-ie-counties.py [-h] [--county COUNTY] [--days DAYS]

optional arguments:
  -h, --help       show this help message and exit
  --county COUNTY  county name - default: Cork
  --days DAYS      number of days to display data for - default: 30
```

```
$ python3 covid-ie-counties.py --county Dublin --days 30
```
