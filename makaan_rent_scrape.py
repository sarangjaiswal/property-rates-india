# import library
import pandas as pd
import requests
from bs4 import BeautifulSoup

# data frame display options on terminal output for debugging
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)

# data frame
df_maakan_price = pd.DataFrame()

# url
maakan_url = 'http://www.makaan.com/price-trends'

# headers (simulate a html browser. get this details from https://www.whoishostingthis.com/tools/user-agent/)
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }

# get the response
response = requests.get(maakan_url, headers=headers)

# get the html content from the response
soup = BeautifulSoup(response.content, "html.parser")
price_table = soup.find('table', class_='tbl', id='city_rent')
table_head = price_table('thead')
table_body = price_table('tbody')

city_name = []
one_bhk_rent_range = []
one_bhk_avg_rent = []
two_bhk_rent_range = []
two_bhk_avg_rent = []
three_bhk_rent_range = []
three_bhk_avg_rent = []

for row in table_body[0].find_all('tr'):
    city_name.append(row.findAll('td')[0].text.strip())
    one_bhk_rent_range.append(row.findAll('td')[1].text.strip().replace(',', ''))
    one_bhk_avg_rent.append(row.findAll('td')[2].text.strip().replace(',', ''))
    two_bhk_rent_range.append(row.findAll('td')[3].text.strip().replace(',', ''))
    two_bhk_avg_rent.append(row.findAll('td')[4].text.strip().replace(',', ''))
    three_bhk_rent_range.append(row.findAll('td')[5].text.strip().replace(',', ''))
    three_bhk_avg_rent.append(row.findAll('td')[6].text.strip().replace(',', ''))


df_maakan_price['city_name'] = city_name
df_maakan_price['one_bhk_rent_range'] = one_bhk_rent_range
df_maakan_price['one_bhk_avg_rent'] = one_bhk_avg_rent
df_maakan_price['two_bhk_rent_range'] = two_bhk_rent_range
df_maakan_price['two_bhk_avg_rent'] = two_bhk_avg_rent
df_maakan_price['three_bhk_rent_range'] = three_bhk_rent_range
df_maakan_price['three_bhk_avg_rent'] = three_bhk_avg_rent


df_maakan_price.to_csv('makaan_price.csv', index=False)
