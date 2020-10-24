import argparse
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

df = pd.read_csv(filename)

# Filter data by county and number of days
df1 = df.loc[df['CountyName'] == args.county]
df2 = df1.tail(args.days)

# Bar Chart - Cumulative Confirmed Cases By County
plt.bar(df2["TimeStamp"], df2["ConfirmedCovidCases"])

plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Cumulative Confirmed Cases for ' + args.county + ' for last ' + str(args.days) + ' days')
plt.show()

# Bar Chart - New Confirmed Cases By County
plt.bar(df2["TimeStamp"], df2["ConfirmedCovidCases"].diff())
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('New Confirmed Cases for ' + args.county + ' for last ' + str(args.days) + ' days')
plt.show()
