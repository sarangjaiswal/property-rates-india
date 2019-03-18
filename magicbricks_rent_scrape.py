# import library
import pandas as pd
import requests
from bs4 import BeautifulSoup

# data frame display options on terminal output for debugging
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)

# data frame
df_magic_bricks_price = pd.DataFrame()

# url
url_magic_bricks = 'https://www.magicbricks.com'
base_magic_bricks_url = 'https://www.magicbricks.com/Property-Rates-Trends'

# set are unique
set_url_magic_bricks = set()
set_sub_url_magic_bricks = set()
list_all_url = []

# headers (simulate a html browser. get this details from https://www.whoishostingthis.com/tools/user-agent/)
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }

# get the response
base_response = requests.get(base_magic_bricks_url, headers=headers)

# get the html content from the response
soup = BeautifulSoup(base_response.content, "html.parser")
base_url_container = soup.find('div', class_='rateTrandsTabData', id='rateTrandsResidential')

# store the city wise urls to a list
for url in base_url_container.find_all('a'):
    set_url_magic_bricks.add(url_magic_bricks + url.get('href'))


for url in set_url_magic_bricks:
    base_response_1 = requests.get(url, headers=headers)
    soup_1 = BeautifulSoup(base_response_1.content, "html.parser")
    base_url_pagination = soup_1.find('div', class_='refinePaging trends-pagination', id='pagination')

    for url_1 in base_url_pagination.find_all('a'):
        # if the url contains 'Page-1' substring then ignore it since we already have that url
        if url_1.get('href').find("Page-1") == -1:
            set_sub_url_magic_bricks.add(url_magic_bricks + url_1.get('href'))
        else:
            pass  # ignore


# merging 2 sets and removing unique and converting the set to list and then sorting it
list_all_url = list(set_sub_url_magic_bricks.union(set_url_magic_bricks))
list_all_url.sort()

city_name = []
locality_name = []
price_range = []
avg_price = []


# loop all the city pages and get the rental price for each locality within city
for url in list_all_url:
    city_name_str = url.split('/')[4].split('-')[-1]
    # get the response
    response = requests.get(url, headers=headers)
    # get the html content from the response
    soup = BeautifulSoup(response.content, "html.parser")
    locality_name_table = soup.find('div', class_='priceTable1 priceTable1-newWidth ', id='localityTable')
    price_table = soup.find('div', class_='priceTable2 priceTable2-newWidth', id='saleTable')

    locality_table_body = locality_name_table('tbody', id='localitySec')
    price_table_body = price_table('tbody')

    for row in locality_table_body[0].find_all('tr'):
        if row.findAll('td'):
            city_name.append(city_name_str.strip())
            locality_name.append(row.findAll('td')[0].text.replace(',', '').strip())
        else:
            pass  # ignore

    for row in price_table_body[0].find_all('tr')[2:]:
        if row.findAll('td'):
            price_range.append(row.findAll('td')[0].text.replace(',', '').strip())
            avg_price.append(row.findAll('td')[1].text.replace(',', '').strip())
        else:
            pass  # ignore


df_magic_bricks_price['city_name'] = city_name
df_magic_bricks_price['locality_name'] = locality_name

df_magic_bricks_price['price_range'] = price_range
df_magic_bricks_price['avg_price'] = avg_price

df_magic_bricks_price.to_csv('magic_bricks_price.csv', index=False)

