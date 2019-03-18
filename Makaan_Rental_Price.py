# import library (if these are not installed then install them using requirements.txt)
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import sqlite3
import datetime
import logging

# get the current time
cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

# get current directory path
cur_dir = os.path.dirname(os.path.realpath(__file__))

# setting the logging level
logging.basicConfig(filename=cur_dir+"/logs/property-rates-india.log",
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

# sqlite3 db path
db = sqlite3.connect(cur_dir + '/db/property_price.db')

# makaan.com website url's
makaan_url = 'http://www.makaan.com'
makaan_price_trend_url = 'http://www.makaan.com/price-trends'

# pandas data frame display options on terminal (this is helpful while debugging)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)

# initializing a data frame
df_makaan_price = pd.DataFrame()

# initializing lists (these are columns in data frame)
scrape_time = []
city_name = []
one_bhk_rent_range = []
one_bhk_avg_rent = []
two_bhk_rent_range = []
two_bhk_avg_rent = []
three_bhk_rent_range = []
three_bhk_avg_rent = []

# headers (simulate a html browser. get this details from https://www.whoishostingthis.com/tools/user-agent/)
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }

# get the response
response = requests.get(makaan_price_trend_url, headers=headers)
logging.debug(f"Received GET Response from {makaan_price_trend_url}")

# get the html content from the response
soup = BeautifulSoup(response.content, "html.parser")
price_table = soup.find('table', class_='tbl', id='city_rent')
table_body = price_table('tbody')
logging.debug(f"Extracted Table and Table body from {makaan_price_trend_url}")

# navigate the table to extract the data from the table.
# the data is extracted per column and stored in a list which is later added to panda's data frame.
for row in table_body[0].find_all('tr'):
    city_name.append(row.findAll('td')[0].text.strip())
    scrape_time.append(cur_time)
    one_bhk_rent_range.append(row.findAll('td')[1].text.strip().replace(',', ''))
    one_bhk_avg_rent.append(row.findAll('td')[2].text.strip().replace(',', ''))
    two_bhk_rent_range.append(row.findAll('td')[3].text.strip().replace(',', ''))
    two_bhk_avg_rent.append(row.findAll('td')[4].text.strip().replace(',', ''))
    three_bhk_rent_range.append(row.findAll('td')[5].text.strip().replace(',', ''))
    three_bhk_avg_rent.append(row.findAll('td')[6].text.strip().replace(',', ''))

logging.debug(f"Scraped data and saved into List")

# adding lists to panda's data frame
df_makaan_price['scrape_time'] = scrape_time
df_makaan_price['city_name'] = city_name
df_makaan_price['one_bhk_rent_range'] = one_bhk_rent_range
df_makaan_price['one_bhk_avg_rent'] = one_bhk_avg_rent
df_makaan_price['two_bhk_rent_range'] = two_bhk_rent_range
df_makaan_price['two_bhk_avg_rent'] = two_bhk_avg_rent
df_makaan_price['three_bhk_rent_range'] = three_bhk_rent_range
df_makaan_price['three_bhk_avg_rent'] = three_bhk_avg_rent
logging.debug(f"Added data to pandas data frame. Shape = {df_makaan_price.shape}")

# saving the data frame to .csv file
df_makaan_price.to_csv(cur_dir + '/csv/makaan_price.csv', index=False)
logging.debug(f"Saving csv file at {cur_dir + '/csv/makaan_price.csv'}")

# appending the data in sqlite3 db
chunks = pd.read_csv(cur_dir + '/csv/makaan_price.csv', chunksize=100)
for chunk in chunks:
    chunk.to_sql('makaan', db, if_exists='append')
logging.debug(f"Appending data into db")
