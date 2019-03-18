# Property Prices in India

Scrape Property Trend Table from Popular property websites in India such as **Makaan.com**, **99Acers.com**, **MagicBricks.com** and save into `CSV` and `SQLite3` file.

## Installation

This is a **Python 3.6** module that depends on the **Beautiful Soup** and **requests** packages.

1. Clone and `cd` into this repo.
2. Install **Python 3.6**.
3. Install requirements from pip with `python3 -m pip install -r requirements.txt`.
4. Test the program by running `python3 Makaan_Rental_Price.py`.

## Usage

Just run `Makaan_Rental_Price.py` file. The output will all be written to the file named `makaan_price.csv` under csv folder. The data will also be appended to the `SQLite3` at `\db\property_price.db`

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