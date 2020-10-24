import argparse
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--county", help="county name - default: Cork", default="Cork")
parser.add_argument("--days", help="number of days to display data for - default: 30", type=int, default="30")
args = parser.parse_args()

# Get latest county date in csv format
filename = 'covid-ie-counties.csv'
data_url = 'https://opendata-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D'
data_content = requests.get(data_url).content
csv_file = open(filename, 'wb')
csv_file.write(data_content)
csv_file.close()

# Filter data by county and number of days
df = pd.read_csv(filename)
df = df.loc[df['CountyName'] == args.county].tail(args.days)

# Converting time stamp to a to datetime e.g. 2020/03/22 00:00:0
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], format='%Y/%m/%d %H:%M:%S')

# Bar Chart - Cumulative Confirmed Cases By County
plt.bar(df["TimeStamp"], df["ConfirmedCovidCases"])
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Cumulative Confirmed Cases for ' + args.county + ' for last ' + str(args.days) + ' days')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.gcf().autofmt_xdate()
plt.show()

# Bar Chart - New Confirmed Cases By County
plt.bar(df["TimeStamp"], df["ConfirmedCovidCases"].diff())
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('New Confirmed Cases for ' + args.county + ' for last ' + str(args.days) + ' days')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.gcf().autofmt_xdate()
plt.show()
