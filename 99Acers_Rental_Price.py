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

# 99acers.com website url's
ninety_nine_acers_url = 'https://www.99acres.com'
ninety_nine_acers_price_trend_url = 'https://www.99acres.com/real-estate-property-rates-index'

# pandas data frame display options on terminal (this is helpful while debugging)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)

# initializing a data frame
df_ninety_nine_acers_price = pd.DataFrame()

# 99acers.com has Property Rates & Price Trends divided into cities.
list_ninety_nine_acers_price_trend_url = []

# initializing lists (these are columns in data frame)
scrape_time = []
city_name = []
locality_name = []
one_bhk_rent_range = []
two_bhk_rent_range = []
three_bhk_rent_range = []

# headers (simulate a html browser. get this details from https://www.whoishostingthis.com/tools/user-agent/)
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }

# get the response
base_response = requests.get(ninety_nine_acers_price_trend_url, headers=headers)
logging.debug(f"Received GET Response from {ninety_nine_acers_price_trend_url}")

# get the html content from the response
soup = BeautifulSoup(base_response.content, "html.parser")
all_cities_container = soup.find('div', class_='cTListContainer')
logging.debug(f"Extracted Div which contains links for cities from {ninety_nine_acers_price_trend_url}")

# get all the property trends by cities url on 99Acers.com
for url in all_cities_container.find_all('a'):
    list_ninety_nine_acers_price_trend_url.append(ninety_nine_acers_url + url.get('href'))


# loop all the city pages and get the rental price for each locality within city
for city_url in list_ninety_nine_acers_price_trend_url:
    # get the response
    response = requests.get(city_url, headers=headers)
    city_name_str = city_url.split('-')[-1]
    logging.debug(f"Navigating to 99acers.com Property Trend page for {city_name_str}")

    # get the html content from the response
    soup = BeautifulSoup(response.content, "html.parser")
    price_table = soup.find('table', class_='prTble')
    table_body = price_table('tbody')

    # navigate the table to extract the data from the table.
    # the data is extracted per column and stored in a list which is later added to panda's data frame.
    for row in table_body[0].find_all('tr'):
        if row.findAll('td'):
            scrape_time.append(cur_time)
            city_name.append(city_name_str.strip())
            locality_name.append(row.findAll('td')[0].text.replace(',', '').replace('Rs. ', '').strip())
            one_bhk_rent_range.append(row.findAll('td')[4].text.replace(',', '').strip())
            two_bhk_rent_range.append(row.findAll('td')[5].text.replace(',', '').strip())
            three_bhk_rent_range.append(row.findAll('td')[6].text.replace(',', '').strip())
        else:
            pass  # ignore

    logging.debug(f"Completed Scraping data from 99acers.com Property Trend page for {city_name_str}")

logging.debug(f"Scraped data and saved into List")

# adding lists to panda's data frame
df_ninety_nine_acers_price['scrape_time'] = scrape_time
df_ninety_nine_acers_price['city_name'] = city_name
df_ninety_nine_acers_price['locality_name'] = locality_name
df_ninety_nine_acers_price['one_bhk_rent_range'] = one_bhk_rent_range
df_ninety_nine_acers_price['two_bhk_rent_range'] = two_bhk_rent_range
df_ninety_nine_acers_price['three_bhk_rent_range'] = three_bhk_rent_range
logging.debug(f"Added data to pandas data frame. Shape = {df_ninety_nine_acers_price.shape}")

# saving the data frame to .csv file
df_ninety_nine_acers_price.to_csv(cur_dir + '/csv/99acres_price.csv', index=False)
logging.debug(f"Saving csv file at {cur_dir + '/csv/99acres_price.csv'}")

# appending the data in sqlite3 db
chunks = pd.read_csv(cur_dir + '/csv/99acres_price.csv', chunksize=100)
for chunk in chunks:
    chunk.to_sql('99acers', db, if_exists='append')
logging.debug(f"Appending data into db")
