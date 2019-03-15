# import libary
import urllib3
import requests
from bs4 import BeautifulSoup
import pandas as pd

# dataframe

# url
maakan_url = 'http://www.makaan.com/price-trends';

# headers (simulate a html browser. get this details from https://www.whoishostingthis.com/tools/user-agent/)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

# get the response
response = requests.get(maakan_url, headers = headers)

# get the html content from the response
soup = BeautifulSoup(response.content, "html.parser")
price_table = soup.find('table', class_='tbl')
table_head = price_table('thead')
table_body = price_table('tbody')


for row in table_head[0].find_all('tr'):
    for cell in row.find_all('th'):
        print(cell.text)
    print('\n')

'''
# create a csv file
with open('makaan_price.csv', 'w') as r:
    for row in table_body[0].find_all('tr'):
        for cell in row.find_all('td'):
            r.write(cell.text)
        r.write('\n')
'''