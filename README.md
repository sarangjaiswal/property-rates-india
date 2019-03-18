# Property Prices in India

Scrape Property Trend Table from Popular property websites in India such as **Makaan.com**, **99Acers.com**, **MagicBricks.com** and save into `CSV` and `SQLite3` file.

## Installation

This is a **Python 3.6** module that depends on the **Beautiful Soup** and **requests** packages.

1. Clone and `cd` into this repo.
2. Install **Python 3.6**.
3. Install requirements from pip with `python3 -m pip install -r requirements.txt`.
4. Test the program by running `python3 Makaan_Rental_Price.py` or `python3 99Acers_Rental_Price.py`. 

## Usage

Just run `Makaan_Rental_Price.py` or `99Acers_Rental_Price.py` file. The output will be written to the file named `makaan_price.csv` or `99acers_price.csv` under `\csv` folder. The data will also be appended to the `SQLite3` at `\db\property_price.db`

I have added logging so that its easier to debug in case you are facing issues. Logs can be found at `/logs/property-rates-india.log`


```text
2019-03-18 11:37:30,727:DEBUG:Starting new HTTP connection (1): www.makaan.com:80
2019-03-18 11:37:31,249:DEBUG:http://www.makaan.com:80 "GET /price-trends HTTP/1.1" 301 185
2019-03-18 11:37:31,251:DEBUG:Starting new HTTPS connection (1): www.makaan.com:443
2019-03-18 11:37:31,602:DEBUG:https://www.makaan.com:443 "GET /price-trends HTTP/1.1" 200 None
2019-03-18 11:37:31,676:DEBUG:Received GET Response from http://www.makaan.com/price-trends
2019-03-18 11:37:32,820:DEBUG:Extracted Table and Table body from http://www.makaan.com/price-trends
2019-03-18 11:37:32,871:DEBUG:Scraped data and saved into List
2019-03-18 11:37:32,875:DEBUG:Added data to pandas data frame. Shape = (339, 8)
2019-03-18 11:37:32,880:DEBUG:Saving csv file at \Python\property-rates-india/csv/makaan_price.csv
2019-03-18 11:37:34,000:DEBUG:Appending data into db
2019-03-18 14:41:04,778:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:05,492:DEBUG:https://www.99acres.com:443 "GET /real-estate-property-rates-index HTTP/1.1" 200 17800
2019-03-18 14:41:05,505:DEBUG:Received GET Response from https://www.99acres.com/real-estate-property-rates-index
2019-03-18 14:41:05,558:DEBUG:Extracted Div which contains links for cities from https://www.99acres.com/real-estate-property-rates-index
2019-03-18 14:41:05,560:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:05,937:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-delhi-ncr HTTP/1.1" 200 25537
2019-03-18 14:41:05,945:DEBUG:Navigating to 99acers.com Property Trend page for ncr
2019-03-18 14:41:06,227:DEBUG:Completed Scraping data from 99acers.com Property Trend page for ncr
2019-03-18 14:41:06,230:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:07,465:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-gurgaon HTTP/1.1" 200 24687
2019-03-18 14:41:07,472:DEBUG:Navigating to 99acers.com Property Trend page for gurgaon
2019-03-18 14:41:07,610:DEBUG:Completed Scraping data from 99acers.com Property Trend page for gurgaon
2019-03-18 14:41:07,613:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:11,063:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-noida HTTP/1.1" 200 22712
2019-03-18 14:41:11,070:DEBUG:Navigating to 99acers.com Property Trend page for noida
2019-03-18 14:41:11,177:DEBUG:Completed Scraping data from 99acers.com Property Trend page for noida
2019-03-18 14:41:11,180:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:12,425:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-greater-noida HTTP/1.1" 200 21495
2019-03-18 14:41:12,431:DEBUG:Navigating to 99acers.com Property Trend page for noida
2019-03-18 14:41:12,511:DEBUG:Completed Scraping data from 99acers.com Property Trend page for noida
2019-03-18 14:41:12,514:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:12,925:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-ghaziabad HTTP/1.1" 200 22421
2019-03-18 14:41:12,932:DEBUG:Navigating to 99acers.com Property Trend page for ghaziabad
2019-03-18 14:41:13,040:DEBUG:Completed Scraping data from 99acers.com Property Trend page for ghaziabad
2019-03-18 14:41:13,043:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:13,397:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-faridabad HTTP/1.1" 200 20577
2019-03-18 14:41:13,403:DEBUG:Navigating to 99acers.com Property Trend page for faridabad
2019-03-18 14:41:13,471:DEBUG:Completed Scraping data from 99acers.com Property Trend page for faridabad
2019-03-18 14:41:13,473:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:13,944:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-mumbai HTTP/1.1" 200 50345
2019-03-18 14:41:13,953:DEBUG:Navigating to 99acers.com Property Trend page for mumbai
2019-03-18 14:41:14,454:DEBUG:Completed Scraping data from 99acers.com Property Trend page for mumbai
2019-03-18 14:41:14,476:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:14,948:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-bangalore HTTP/1.1" 200 32524
2019-03-18 14:41:14,956:DEBUG:Navigating to 99acers.com Property Trend page for bangalore
2019-03-18 14:41:15,198:DEBUG:Completed Scraping data from 99acers.com Property Trend page for bangalore
2019-03-18 14:41:15,201:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:18,821:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-chennai HTTP/1.1" 200 27591
2019-03-18 14:41:18,835:DEBUG:Navigating to 99acers.com Property Trend page for chennai
2019-03-18 14:41:19,035:DEBUG:Completed Scraping data from 99acers.com Property Trend page for chennai
2019-03-18 14:41:19,038:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:20,260:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-hyderabad HTTP/1.1" 200 23080
2019-03-18 14:41:20,265:DEBUG:Navigating to 99acers.com Property Trend page for hyderabad
2019-03-18 14:41:20,370:DEBUG:Completed Scraping data from 99acers.com Property Trend page for hyderabad
2019-03-18 14:41:20,373:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:26,820:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-pune HTTP/1.1" 200 32360
2019-03-18 14:41:26,827:DEBUG:Navigating to 99acers.com Property Trend page for pune
2019-03-18 14:41:27,102:DEBUG:Completed Scraping data from 99acers.com Property Trend page for pune
2019-03-18 14:41:27,105:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:27,533:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-kolkata HTTP/1.1" 200 26444
2019-03-18 14:41:27,545:DEBUG:Navigating to 99acers.com Property Trend page for kolkata
2019-03-18 14:41:27,714:DEBUG:Completed Scraping data from 99acers.com Property Trend page for kolkata
2019-03-18 14:41:27,716:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:32,423:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-ahmedabad HTTP/1.1" 200 23088
2019-03-18 14:41:32,429:DEBUG:Navigating to 99acers.com Property Trend page for ahmedabad
2019-03-18 14:41:32,533:DEBUG:Completed Scraping data from 99acers.com Property Trend page for ahmedabad
2019-03-18 14:41:32,535:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:33,976:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-bhubaneswar HTTP/1.1" 200 19900
2019-03-18 14:41:33,982:DEBUG:Navigating to 99acers.com Property Trend page for bhubaneswar
2019-03-18 14:41:34,040:DEBUG:Completed Scraping data from 99acers.com Property Trend page for bhubaneswar
2019-03-18 14:41:34,042:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:34,625:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-coimbatore HTTP/1.1" 200 19811
2019-03-18 14:41:34,631:DEBUG:Navigating to 99acers.com Property Trend page for coimbatore
2019-03-18 14:41:34,687:DEBUG:Completed Scraping data from 99acers.com Property Trend page for coimbatore
2019-03-18 14:41:34,689:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:36,143:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-indore HTTP/1.1" 200 20384
2019-03-18 14:41:36,149:DEBUG:Navigating to 99acers.com Property Trend page for indore
2019-03-18 14:41:36,212:DEBUG:Completed Scraping data from 99acers.com Property Trend page for indore
2019-03-18 14:41:36,214:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:37,901:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-nagpur HTTP/1.1" 200 21905
2019-03-18 14:41:37,907:DEBUG:Navigating to 99acers.com Property Trend page for nagpur
2019-03-18 14:41:38,010:DEBUG:Completed Scraping data from 99acers.com Property Trend page for nagpur
2019-03-18 14:41:38,016:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:38,427:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-vadodara HTTP/1.1" 200 21524
2019-03-18 14:41:38,433:DEBUG:Navigating to 99acers.com Property Trend page for vadodara
2019-03-18 14:41:38,583:DEBUG:Completed Scraping data from 99acers.com Property Trend page for vadodara
2019-03-18 14:41:38,585:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:39,158:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-chandigarh HTTP/1.1" 200 20192
2019-03-18 14:41:39,170:DEBUG:Navigating to 99acers.com Property Trend page for chandigarh
2019-03-18 14:41:39,234:DEBUG:Completed Scraping data from 99acers.com Property Trend page for chandigarh
2019-03-18 14:41:39,236:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:39,613:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-jaipur HTTP/1.1" 200 21039
2019-03-18 14:41:39,619:DEBUG:Navigating to 99acers.com Property Trend page for jaipur
2019-03-18 14:41:39,700:DEBUG:Completed Scraping data from 99acers.com Property Trend page for jaipur
2019-03-18 14:41:39,703:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:40,965:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-lucknow HTTP/1.1" 200 20751
2019-03-18 14:41:40,973:DEBUG:Navigating to 99acers.com Property Trend page for lucknow
2019-03-18 14:41:41,045:DEBUG:Completed Scraping data from 99acers.com Property Trend page for lucknow
2019-03-18 14:41:41,048:DEBUG:Starting new HTTPS connection (1): www.99acres.com:443
2019-03-18 14:41:42,754:DEBUG:https://www.99acres.com:443 "GET /property-rates-and-price-trends-in-surat HTTP/1.1" 200 20449
2019-03-18 14:41:42,759:DEBUG:Navigating to 99acers.com Property Trend page for surat
2019-03-18 14:41:42,830:DEBUG:Completed Scraping data from 99acers.com Property Trend page for surat
2019-03-18 14:41:42,830:DEBUG:Scraped data and saved into List
2019-03-18 14:41:42,834:DEBUG:Added data to pandas data frame. Shape = (2406, 6)
2019-03-18 14:41:42,849:DEBUG:Saving csv file at property-rates-india/csv/99acres_price.csv
2019-03-18 14:41:50,610:DEBUG:Appending data into db
```

## Sample Results

#### Snippet from makaan_price.csv

```text
scrape_time,city_name,one_bhk_rent_range,one_bhk_avg_rent,two_bhk_rent_range,two_bhk_avg_rent,three_bhk_rent_range,three_bhk_avg_rent
2019-03-18 11:37,Ahmedabad,2500 - 30000,10285.71,3500 - 78000,14345.28,5000 - 1.5 L,42406.05
2019-03-18 11:37,Bangalore,2000 - 5 L,11532.47,5000 - 61111,15737.24,8500 - 2 L,34379.6
2019-03-18 11:37,Chennai,2000 - 5 L,11970.9,5500 - 39000,14454.87,6000 - 1.4 L,30851.65
2019-03-18 11:37,Delhi,3000 - 1 L,14113.04,4850 - 1.4 L,20671.43,4500 - 4.8 L,96794.87
2019-03-18 11:37,Ghaziabad,3500 - 13000,6877.78,4500 - 20000,10168,13000 - 31000,18312.5
2019-03-18 11:37,Gurgaon,2000 - 35000,12752,6000 - 2.5 L,23943.95,13000 - 71000,31909.09
2019-03-18 11:37,Hyderabad,3500 - 1.4 L,11678.12,5000 - 95000,13322.69,9000 - 75000,23701.61
2019-03-18 11:37,Indore,4000 - 85000,13918.18,5000 - 50000,13857.14,7000 - 40000,15411.76
2019-03-18 11:37,Kolkata,3000 - 96000,10890.36,3500 - 65000,12327.3,10000 - 1.5 L,31400
2019-03-18 11:37,Mumbai,2000 - 1 L,15693.65,5000 - 1.6 L,33176,12000 - 4.5 L,103000
2019-03-18 11:37,Noida,4500 - 25000,10462.39,6500 - 35000,1896.34,7000 - 55000,23614.77
2019-03-18 11:37,Pune,1900 - 50000,10892.11,4500 - 1.2 L,26833.15,5000 - 2 L,50277.06
```
#### Snippet from 99acers_price.csv

```text
scrape_time,city_name,locality_name,one_bhk_rent_range,two_bhk_rent_range,three_bhk_rent_range
2019-03-18 14:41,ncr,Akshardham,-,-,Rs. 45900 - 52700
2019-03-18 14:41,ncr,Dilshad Colony,-,-,-
2019-03-18 14:41,ncr,Dilshad Garden,-,Rs. 10771 - 12118,-
2019-03-18 14:41,ncr,I P Extension,Rs. 10710 - 11900,Rs. 16150 - 17000,Rs. 19202 - 21335
2019-03-18 14:41,ncr,Kondli Gharoli,-,Rs. 7039 - 8122,-
2019-03-18 14:41,ncr,Mayur Vihar - I,Rs. 11602 - 13812,Rs. 18700 - 21250,Rs. 22950 - 26392
2019-03-18 14:41,ncr,Mayur Vihar - II,Rs. 9528 - 11534,Rs. 14450 - 17000,Rs. 18091 - 20220
2019-03-18 14:41,ncr,Mayur Vihar - III,-,Rs. 8976 - 10771,-
2019-03-18 14:41,ncr,New Ashok Nagar,Rs. 10518 - 13719,-,-
2019-03-18 14:41,ncr,Patparganj,Rs. 8670 - 10200,Rs. 16150 - 17000,Rs. 21237 - 23473
2019-03-18 14:41,ncr,Preet Vihar,Rs. 6078 - 7735,-,-
2019-03-18 14:41,ncr,Vasundhara Enclave,Rs. 10710 - 13770,Rs. 16150 - 17850,Rs. 19580 - 21883
2019-03-18 14:41,ncr,A1 Block Paschim Vihar,-,Rs. 10901 - 12622,-
2019-03-18 14:41,ncr,Bakkarwala,-,-,-
```