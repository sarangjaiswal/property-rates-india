# import library
import pandas as pd
import requests
from bs4 import BeautifulSoup

# data frame display options on terminal output for debugging
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)

# data frame
df_99acres_price = pd.DataFrame()

# base url
url_99acres = 'https://www.99acres.com'
base_url_99acres = 'https://www.99acres.com/real-estate-property-rates-index'
list_url_99acres = []

# headers (simulate a html browser. get this details from https://www.whoishostingthis.com/tools/user-agent/)
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }

# get the response
base_response = requests.get(base_url_99acres, headers=headers)

# get the html content from the response
soup = BeautifulSoup(base_response.content, "html.parser")
base_url_container = soup.find('div', class_='cTListContainer')

# store the city wise urls to a list
for url in base_url_container.find_all('a'):
    list_url_99acres.append(url_99acres + url.get('href'))


city_name = []
locality_name = []
one_bhk_rent_range = []
two_bhk_rent_range = []
three_bhk_rent_range = []

# loop all the city pages and get the rental price for each locality within city
for url in list_url_99acres:
    # get the response
    response = requests.get(url, headers=headers)
    city_name_str = url.split('-')[-1]

    # get the html content from the response
    soup = BeautifulSoup(response.content, "html.parser")
    price_table = soup.find('table', class_='prTble')
    table_head = price_table('thead')
    table_body = price_table('tbody')

    for row in table_body[0].find_all('tr'):
        if row.findAll('td'):
            city_name.append(city_name_str.strip())
            locality_name.append(row.findAll('td')[0].text.replace(',', '').replace('Rs. ', '').strip())
            one_bhk_rent_range.append(row.findAll('td')[4].text.replace(',', '').strip())
            two_bhk_rent_range.append(row.findAll('td')[5].text.replace(',', '').strip())
            three_bhk_rent_range.append(row.findAll('td')[6].text.replace(',', '').strip())
        else:
            pass # ignore

df_99acres_price['city_name'] = city_name
df_99acres_price['locality_name'] = locality_name
df_99acres_price['one_bhk_rent_range'] = one_bhk_rent_range
df_99acres_price['two_bhk_rent_range'] = two_bhk_rent_range
df_99acres_price['three_bhk_rent_range'] = three_bhk_rent_range

df_99acres_price.to_csv('99acres_price.csv', index=False)



