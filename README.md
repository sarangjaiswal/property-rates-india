# Property Prices in India

Scrape Property Trend Table from Popular property websites in India such as **Makaan.com**, **99acers.com** and save into CSV file.


## Installation

This is a **Python 3.6** module that depends on the **Beautiful Soup** and **requests** packages.

1. Clone and `cd` into this repo.
2. Install **Python 3.6**.
3. Install requirements from pip with `python3 -m pip install -r requirements.txt`.
4. Test the program by running `python3 scrape.py`.

## Usage

Just run `makaan_rent_scrape.py` file. The output will all be written to the file named `makaan_price.csv`.

Inspecting the output with Bash gives the following results:

```text
SarangMac:property-rates-india sarangjaiswal$ ls
99acres_price.csv       LICENSE                 makaan_price.csv        requirements.txt
99acres_rent_scrape.py  README.md               makaan_rent_scrape.py
SarangMac:property-rates-india sarangjaiswal$ tree
.
├── 99acres_price.csv
├── 99acres_rent_scrape.py
├── LICENSE
├── README.md
├── makaan_price.csv
├── makaan_rent_scrape.py
└── requirements.txt

0 directories, 7 files
```
## Sample Result

### makaan_price.csv

```text
city_name,one_bhk_rent_range,one_bhk_avg_rent,two_bhk_rent_range,two_bhk_avg_rent,three_bhk_rent_range,three_bhk_avg_rent
Ahmedabad,2500 - 30000,10285.71,3500 - 78000,14345.28,5000 - 1.5 L,42406.05
Bangalore,2000 - 5 L,11532.47,5000 - 61111,15737.24,8500 - 2 L,34379.6
Chennai,2000 - 5 L,11970.9,5500 - 39000,14454.87,6000 - 1.4 L,30851.65
Delhi,3000 - 1 L,14113.04,4850 - 1.4 L,20671.43,4500 - 4.8 L,96794.87
Ghaziabad,3500 - 13000,6877.78,4500 - 20000,10168,13000 - 31000,18312.5
Gurgaon,2000 - 35000,12752,6000 - 2.5 L,23943.95,13000 - 71000,31909.09
Hyderabad,3500 - 1.4 L,11678.12,5000 - 95000,13322.69,9000 - 75000,23701.61
Indore,4000 - 85000,13918.18,5000 - 50000,13857.14,7000 - 40000,15411.76
Kolkata,3000 - 96000,10890.36,3500 - 65000,12327.3,10000 - 1.5 L,31400
Mumbai,2000 - 1 L,15693.65,5000 - 1.6 L,33176,12000 - 4.5 L,103000
Noida,4500 - 25000,10462.39,6500 - 35000,1896.34,7000 - 55000,23614.77
Pune,1900 - 50000,10892.11,4500 - 1.2 L,26833.15,5000 - 2 L,50277.06
Jalandhar,5000 - 8500,6200,15000 - 25000,20750,17000,17000
Lucknow,3500 - 30000,10467.74,4000 - 40000,12342.76,6000 - 45000,19920
Chandigarh,5000 - 18000,12500,8500 - 45000,16825,16000 - 1.5 L,69692.31
Nagpur,3000 - 17000,8477.53,6000 - 40000,12578.95,9000 - 45000,18220
Coimbatore,5000 - 15000,8670.83,8000 - 20000,11416.67,15000 - 20000,17250
Goa,12000,12000,22000 - 55000,30333.33,17000 - 80000,34815.79
Jaipur,4493 - 2.9 L,16781.11,6500 - 2.9 L,18100,10000 - 55000,23680
Trivandrum,5000 - 50000,22000,10000 - 20000,1266.67,9000 - 60000,17961.54
Kochi,8000,8000,8000 - 20000,13500,5000 - 50000,16909.09
Bhubaneswar,5500 - 14000,9357.14,6000 - 15000,10000,5000 - 35000,15444.44
Puri,-,-,-,-,-,-
Bhopal,4000 - 15000,6140,4000 - 80000,17941.18,6000 - 70000,2193.22
Nashik,3500 - 12000,6187.5,6000 - 30000,11437.5,12000 - 42000,2241.67
Mysore,4000 - 23000,12000,8000 - 35000,12760,18000 - 25000,20250
Dehradun,4500 - 20000,12250,9000 - 35000,14892.86,17000 - 28000,20150
Vadodara,3000 - 10000,6525,6000 - 16000,10550,5500 - 48000,15684.78
Mangalore,5000 - 11000,7625,6000 - 20000,10966.67,15000 - 30000,19600
Surat,4000 - 85000,21314.29,8000 - 70000,18791.67,15000 - 90000,37894.17
Visakhapatnam,5000 - 13000,10000,5500 - 20000,11166.67,10000,10000
Anand,-,-,5000 - 10000,7500,16000,16000
Madurai,3000 - 8500,5882.98,4000 - 35000,10257.3,6500 - 30000,1548.54
Patna,3000 - 10000,5857.14,4000 - 4 L,46970,8500 - 50000,24500
Trichy,11000,11000,7000 - 8000,7500,16000 - 20000,18000
Agra,8000,8000,5999 - 12000,9749.75,15000,15000
Pondicherry,3500,3500,6000 - 13000,9500,12000,12000
Shimla,-,-,16000,16000,8000,8000
Kozhikode,-,-,12500,12500,-,-
Kanpur,5000 - 7000,6000,8000 - 15000,11666.67,12000 - 15000,13333.33
Meerut,3000 - 5999,4499.5,4000 - 8000,6000,7000 - 50000,19625
Ranchi,2500 - 10000,6235.29,4000 - 90000,9742.86,6000 - 20000,15375
Vellore,-,-,12000,12000,-,-
Allahabad,3000 - 15001,7500.33,7000 - 15000,9750,12000 - 20000,16750
Gwalior,-,-,5000,5000,10000,10000
Haridwar,50000,50000,5000 - 6000,5666.67,20000,20000
Kannur,-,-,-,-,-,-
Varanasi,5000 - 12000,7500,6000 - 16000,10115.38,13500 - 30000,19687.5
Vijayawada,6500 - 30000,14250,6500 - 16000,1195.43,20000 - 25000,22500
Aurangabad,10000 - 15000,12500,12000 - 15000,13000,15000,15000
Guwahati,6000 - 9000,7666.67,8000 - 25000,13625,13000 - 16000,15000
Jabalpur,5500 - 11000,7125,12000,12000,-,-
Jodhpur,3000 - 70000,10666.67,12000 - 20000,15846.15,12000 - 35000,19647.06
Kolhapur,3500 - 6000,4750,9500,9500,20000,20000
Nainital,10000,10000,-,-,20000,20000
Amritsar,-,-,15000,15000,10000,10000
Jamshedpur,5000 - 7000,6000,5000 - 15000,8240,9000 - 23000,12710.53
Kottayam,-,-,-,-,-,-
Ambala,3000 - 12500,8957.14,30000,30000,26000,26000
Mathura,2000,2000,9000,9000,12000,12000
Alwar,9500,9500,3000 - 6500,5300,-,-
Jhansi,2000,2000,14000,14000,-,-
Faridabad,2600 - 70000,9674.81,7000 - 35000,14437.93,9000 - 90000,25447.06
Anantapuram,-,-,-,-,35000,35000
Sonepat,-,-,7500 - 75000,21300,8000 - 80000,13558.82
Karnal,5500,5500,-,-,17000,17000
Siliguri,7000,7000,7000 - 28000,19000,26500 - 30000,28166.67
Ooty,-,-,-,-,-,-
Aligarh,3000,3000,-,-,10500 - 14000,12250
Thiruvannamalai,-,-,-,-,-,-
Durgapur,15000,15000,6500 - 7000,6750,9000 - 16000,13000
Panipat,5400,5400,6000 - 10000,8571.43,12000,12000
Raigad,2000 - 27000,9283.33,10500,10500,15000,15000
Wayanad,-,-,-,-,-,-
Tirunelveli,-,-,-,-,12000,12000
Ludhiana,3500 - 13000,7797.19,6000 - 30000,14715.81,9000 - 50000,23617.56
Ernakulam,-,-,10000 - 27000,18333.33,16500,16500
Arambagh,-,-,-,-,-,-
Salem,14500,14500,10000,10000,-,-
Dindigul,-,-,-,-,-,-
Warangal,-,-,9000 - 10000,9500,6500,6500
Gulbarga,-,-,-,-,-,-
Tirupati,3500,3500,-,-,-,-
Mehsana,-,-,-,-,-,-
Thrissur,-,-,10000,10000,40000,40000
Satara,2750 - 5500,4250,-,-,-,-
Solapur,4500 - 8600,6550,9500 - 9900,9700,20000,20000
Guntur,3500,3500,8000,8000,1.8 L,180000
Solan,5000 - 7000,6000,6000 - 8000,7000,11000,11000
Jhajjar,-,-,-,-,-,-
Bulandshahr,-,-,-,-,-,-
Ganjam,-,-,-,-,-,-
Bareilly,20000,20000,7000 - 9700,8350,14000,14000
Moradabad,-,-,7000,7000,17000,17000
Almora,11000,11000,15000,15000,25000,25000
Ratnagiri,-,-,-,-,25000,25000
Mandya,-,-,6500,6500,-,-
Hubli Dharwad,4500,4500,10000,10000,24500,24500
Krishna,-,-,-,-,-,-
Valsad,4500 - 5500,5000,6000 - 15000,8405.8,10000 - 16000,12750
Patiala,-,-,8000,8000,-,-
Rohtak,-,-,5000 - 9500,7250,-,-
Bhavnagar,3200 - 7000,4580,6000 - 12000,7722.22,9000 - 10000,9333.33
Rayagada,-,-,-,-,-,-
Bharuch,-,-,-,-,-,-
Dausa,-,-,-,-,-,-
Rishikesh,5000,5000,14000,14000,-,-
Burdwan,8000,8000,9000,9000,15000,15000
Udham Singh Nagar,-,-,7500,7500,-,-
Shahjahanpur,-,-,-,-,-,-
Muzaffarnagar,-,-,-,-,-,-
Hisar,-,-,-,-,-,-
Sirsa,-,-,-,-,22000,22000
Chikkamagaluru,13000,13000,-,-,-,-
Udupi,12500,12500,12000,12000,-,-
Fatehabad,-,-,-,-,-,-
Sangli,3500,3500,7000 - 8000,7500,-,-
Raigarh,25000,25000,11000 - 20000,14600,10000 - 27000,18500
Parbhani,2500,2500,15000,15000,-,-
Osmanabad,-,-,-,-,-,-
Nandurbar,-,-,25000,25000,-,-
Nanded,-,-,-,-,-,-
Kurnool,-,-,12000,12000,-,-
Nellore,-,-,8800,8800,-,-
Nizamabad,-,-,-,-,-,-
Rajahmundry,-,-,-,-,13000 - 16500,14375
Bhagalpur,-,-,-,-,-,-
Raipur,4500 - 9000,6607.14,5500 - 20000,10546.34,10000 - 25700,17380
Gandhinagar,5000,5000,9000,9000,22000 - 40000,31000
Jamnagar,5500,5500,-,-,12000,12000
Porbandar,-,-,-,-,-,-
Rajkot,9000,9000,15000,15000,17000 - 18000,17500
Kurukshetra,3500,3500,-,-,-,-
Panchkula,4000 - 13000,878.65,8000 - 20000,13907.89,11000 - 85000,27125
Dharamsala,-,-,-,-,-,-
Manali,-,-,-,-,-,-
Jammu,-,-,16000,16000,25000,25000
Srinagar,-,-,-,-,-,-
Bokaro,8000,8000,5500 - 8000,6750,-,-
Dhanbad,-,-,4000,4000,6000,6000
Belgaum,6000 - 1.2 L,45333.33,6500 - 10000,7875,16000 - 18000,17000
Bellary,-,-,-,-,-,-
Bidar,-,-,-,-,-,-
Dharwad,-,-,9500,9500,10000,10000
Hubli,-,-,-,-,-,-
Kolar,-,-,-,-,-,-
Alappuzha,-,-,30000,30000,-,-
Kollam,2000,2000,-,-,-,-
Palakkad,6000,6000,6500,6500,-,-
Ujjain,-,-,7500 - 9000,8250,14000,14000
Imphal,35000,35000,-,-,22000,22000
Shillong,-,-,-,-,-,-
Cuttack,18000,18000,4500,4500,5000,5000
Rourkela,10000,10000,-,-,-,-
Mohali,6500 - 12000,9625,10000 - 28000,1913.16,18000 - 48000,27211.54
Pathankot,-,-,-,-,-,-
Ajmer,5000,5000,15000,15000,15000,15000
Bhilwara,-,-,13750,13750,-,-
Kota,7000 - 30000,18500,15000,15000,12000 - 13000,12500
Udaipur,9000,9000,9000 - 15000,12700,21000 - 40000,30500
Gangtok,-,-,-,-,-,-
Erode,10000,10000,-,-,-,-
Hosur,13000,13000,10000,10000,-,-
Agartala,-,-,-,-,2 L,200000
Faizabad,-,-,-,-,-,-
Gorakhpur,-,-,-,-,-,-
Roorkee,5500,5500,-,-,-,-
Dadra and Nagar Haveli,-,-,8500,8500,-,-
Daman and Diu,5000 - 6500,690.91,25000,25000,12000 - 25000,16277.78
Latur,-,-,-,-,-,-
Jalna,-,-,-,-,-,-
Jalgaon,-,-,-,-,-,-
Dhule,-,-,-,-,10000,10000
Chandrapur,-,-,-,-,-,-
Bhandara,2500,2500,3500,3500,-,-
Amravati,7000,7000,7000 - 11000,9000,-,-
Akola,-,-,5500 - 6500,6000,-,-
Ahmednagar,5000,5000,10000,10000,-,-
Sindhudurg,-,-,-,-,-,-
Wardha,-,-,45000,45000,-,-
Washim,-,-,-,-,-,-
Yavatmal,-,-,-,-,-,-
Kodaikanal,-,-,-,-,-,-
Shirdi,6500,6500,-,-,-,-
Zirakpur,7000 - 8000,7500,5500 - 12000,8500,13500 - 28000,18333.33
Baddi,-,-,-,-,-,-
Neemrana,-,-,-,-,-,-
Rewari,16800 - 22400,19133.33,32000,32000,45000,45000
Palwal,7000 - 8500,7750,12000 - 24000,17000,-,-
Karur,-,-,-,-,-,-
Baramati,-,-,7000,7000,-,-
Alibaugh,-,-,15000,15000,-,-
Saharanpur,-,-,10000,10000,50000,50000
Hardoi,-,-,-,-,7500,7500
Rampur,-,-,-,-,-,-
Etawah,-,-,-,-,-,-
Hapur,-,-,-,-,-,-
Gonda,-,-,-,-,-,-
Basti,-,-,-,-,-,-
Mirzapur,-,-,-,-,-,-
Azamgarh,8500 - 13500,11000,13000 - 14000,13666.67,22000,22000
Barabanki,-,-,-,-,-,-
Bahadurgarh,-,-,-,-,10000,10000
Nalgonda,-,-,-,-,-,-
Hassan,7500,7500,17000,17000,18000,18000
Kakinada,-,-,-,-,20000,20000
Shimoga,3500,3500,-,-,-,-
Proddatur,-,-,-,-,-,-
Coorg,-,-,-,-,-,-
Muzaffarpur,-,-,5100 - 6700,5900,10500,10500
Begusarai,2500,2500,-,-,-,-
Durg,7500,7500,11000,11000,-,-
Nokha,-,-,-,-,-,-
Kangra,-,-,-,-,-,-
Bolpur,-,-,-,-,-,-
Dibrugarh,-,-,-,-,-,-
Cuddalore,-,-,-,-,-,-
East Godavari,-,-,-,-,-,-
Tiruppur,9000,9000,9000 - 15000,12333.33,-,-
Chamarajanagar,-,-,-,-,-,-
Koraput,-,-,-,-,-,-
Tuticorin,-,-,-,-,-,-
Pudukkottai,-,-,-,-,-,-
Villupuram,-,-,-,-,-,-
Dharmapuri,-,-,-,-,-,-
Perambalur,-,-,-,-,-,-
Chitradurga,-,-,-,-,-,-
Tumakuru,-,-,8000,8000,-,-
Greater Noida,4000 - 16000,6666.67,5000 - 62000,10357.58,8000 - 30000,15875
Balasore,-,-,-,-,-,-
Bhadrak,-,-,-,-,-,-
Sehore,-,-,-,-,-,-
Asansol,15000,15000,-,-,15000,15000
Nadia,-,-,-,-,-,-
Pathanamthitta,-,-,-,-,16000,16000
Kheda,-,-,-,-,-,-
Belagavi,5000,5000,7000 - 8000,7500,-,-
Bikaner,-,-,15000,15000,-,-
Bhatinda,-,-,-,-,-,-
Eluru,-,-,-,-,-,-
Athens,-,-,-,-,-,-
Chittoor,-,-,-,-,-,-
Jajpur,-,-,-,-,-,-
Vijayapura,-,-,7600,7600,-,-
Rajsamand,-,-,-,-,-,-
Shivamogga,-,-,10500,10500,-,-
Kutch,-,-,10000,10000,-,-
Kanyakumari,-,-,-,-,-,-
Kadapa,-,-,-,-,-,-
Srikakulam,-,-,-,-,-,-
Jharsuguda,-,-,-,-,-,-
Sikar,-,-,-,-,-,-
Gaya,-,-,8500,8500,-,-
Bilaspur,-,-,5500 - 8000,6750,-,-
Darbhanga,-,-,-,-,-,-
Darjeeling,-,-,-,-,-,-
Navsari,-,-,-,-,12000,12000
Ratlam,-,-,-,-,-,-
Junagadh,-,-,-,-,-,-
Hathras,-,-,-,-,-,-
Deoghar,-,-,-,-,-,-
Jhunjhunu,-,-,-,-,-,-
Sambalpur,-,-,-,-,-,-
Barnala,-,-,-,-,-,-
Bankura,-,-,-,-,-,-
Madhubani,-,-,-,-,-,-
Theni,-,-,-,-,-,-
Hazaribagh,-,-,-,-,-,-
Pali,-,-,-,-,-,-
Banswara,-,-,-,-,-,-
Barmer,-,-,-,-,-,-
Purulia,-,-,-,-,-,-
Mewat,-,-,-,-,-,-
West Godavari,-,-,-,-,-,-
Thanjavur,-,-,-,-,-,-
Dera Bassi,-,-,8500 - 12000,10166.67,15000,15000
Sri Ganganagar,-,-,-,-,-,-
Hoshangabad,-,-,-,-,-,-
Beed,-,-,-,-,-,-
Bhiwadi,5000,5000,5000 - 8500,6300,20000,20000
Aruppukkottai,-,-,-,-,-,-
Bagpat,-,-,-,-,-,-
Balotra,-,-,-,-,-,-
Berhampur,-,-,-,-,-,-
Cuttak,-,-,-,-,-,-
Gadag,-,-,-,-,-,-
Gadarwara,-,-,-,-,-,-
Guruvayoor,-,-,-,-,-,-
Hissar,-,-,-,-,-,-
Jalpaiguri,-,-,-,-,-,-
Karwar,-,-,8000,8000,-,-
Khambhat,-,-,-,-,-,-
Kulu Manali,-,-,-,-,-,-
Kumhari,-,-,6000,6000,-,-
Mahesana,-,-,-,-,-,-
Mussoorie,-,-,-,-,-,-
Patan,-,-,-,-,-,-
Prakasham,-,-,-,-,-,-
Tiruvannamalai,-,-,-,-,-,-
Tumkur,-,-,-,-,-,-
Bagru,-,-,-,-,-,-
Buldhana,-,-,-,-,-,-
Amroha,-,-,-,-,-,-
Unnao,-,-,-,-,-,-
Bharatpur,-,-,-,-,-,-
Bhiwani,-,-,-,-,-,-
Davanagere,-,-,-,-,-,-
Fatehpur,-,-,-,-,-,-
Jaunpur,-,-,-,-,-,-
Kasaragod,5000,5000,-,-,-,-
Malappuram,-,-,-,-,-,-
Purnia,-,-,-,-,15000,15000
Raichur,-,-,-,-,-,-
Thoothukudi,-,-,-,-,-,-
Vizianagaram,-,-,-,-,-,-
Yamunanagar,-,-,-,-,-,-
Dharuhera,-,-,6000 - 15000,10500,-,-
Jind,-,-,-,-,-,-
Kaithal,-,-,-,-,-,-
Mithapur,-,-,-,-,-,-
Rupnagar,-,-,-,-,-,-
Sitapur,-,-,-,-,-,-
Kushinagar,-,-,-,-,-,-
Bijapur,-,-,-,-,-,-
Gondia,-,-,-,-,-,-
Krishnagiri,-,-,-,-,-,-
Namakkal,-,-,-,-,-,-
Sivaganga,-,-,-,-,-,-
Nilgiris,-,-,-,-,-,-
Thiruvananthapuram,11000 - 1.2 L,65500,9000,9000,14000,14000
Jangaon,-,-,-,-,-,-
Sangareddy,-,-,-,-,-,-
Sirohi,-,-,-,-,-,-
Aravalli,-,-,-,-,-,-
Dungarpur,-,-,-,-,-,-
Nagaur,-,-,-,-,-,-
Tonk,-,-,-,-,-,-
Jalore,-,-,-,-,-,-
Hanumangarh,-,-,-,-,-,-
```
### 99acres.csv

```text
city_name,locality_name,one_bhk_rent_range,two_bhk_rent_range,three_bhk_rent_range
ncr,Akshardham,-,-,Rs. 45900 - 52700
ncr,Dilshad Colony,-,-,-
ncr,Dilshad Garden,-,Rs. 10771 - 12118,-
ncr,I P Extension,Rs. 10710 - 11900,Rs. 16150 - 17000,Rs. 19202 - 21335
ncr,Kondli Gharoli,-,Rs. 7039 - 8122,-
ncr,Mayur Vihar - I,Rs. 11602 - 13812,Rs. 18700 - 21250,Rs. 22950 - 26392
ncr,Mayur Vihar - II,Rs. 9528 - 11534,Rs. 14450 - 17000,Rs. 18091 - 20220
ncr,Mayur Vihar - III,-,Rs. 8976 - 10771,-
ncr,New Ashok Nagar,Rs. 10518 - 13719,-,-
ncr,Patparganj,Rs. 8670 - 10200,Rs. 16150 - 17000,Rs. 21237 - 23473
ncr,Preet Vihar,Rs. 6078 - 7735,-,-
ncr,Vasundhara Enclave,Rs. 10710 - 13770,Rs. 16150 - 17850,Rs. 19580 - 21883
ncr,A1 Block Paschim Vihar,-,Rs. 10901 - 12622,-
ncr,Bakkarwala,-,-,-
ncr,D Block Vikaspuri,-,-,-
ncr,Janakpuri,Rs. 9125 - 11526,Rs. 13770 - 17595,Rs. 20927 - 26159
ncr,Mahavir Enclave,-,-,-
ncr,Moti Nagar,-,Rs. 20664 - 25360,Rs. 26007 - 29723
ncr,Paschim Vihar,Rs. 8075 - 10200,Rs. 14535 - 16830,Rs. 18528 - 21616
ncr,Patel Nagar,-,Rs. 16830 - 19890,Rs. 21781 - 27009
ncr,Punjabi Bagh,-,-,-
ncr,Ramesh Nagar,-,Rs. 12282 - 14450,-
ncr,Subhash Nagar,Rs. 8394 - 10744,-,-
ncr,Uttam Nagar,-,-,Rs. 8500 - 11050
ncr,Uttam Nagar East,-,-,-
ncr,Uttam Nagar West,-,-,-
ncr,Vikas Puri,Rs. 8160 - 9690,Rs. 12586 - 14807,Rs. 18559 - 20621
ncr,West Patel Nagar,-,Rs. 16083 - 18380,Rs. 22950 - 23906
ncr,Karol Bagh,-,-,-
ncr,Dwarka Mor,-,-,-
ncr,Kakrola,-,-,-
ncr,L Zone,-,-,-
ncr,Pocket-2 Sector 6 Dwarka,-,Rs. 13889 - 16082,-
ncr,Sector-1 Dwarka,-,-,-
ncr,Sector-2 Dwarka,-,Rs. 17809 - 20777,Rs. 21038 - 22440
ncr,Sector-3 Dwarka,-,Rs. 15300 - 18360,Rs. 20260 - 21610
ncr,Sector-4 Dwarka,-,Rs. 17136 - 18088,Rs. 20400 - 23120
ncr,Sector-5 Dwarka,-,-,Rs. 21280 - 24117
ncr,Sector-6 Dwarka,-,Rs. 16830 - 18700,Rs. 20400 - 23120
ncr,Sector-7 Dwarka,Rs. 9818 - 10752,Rs. 17765 - 19635,Rs. 20400 - 24480
ncr,Sector-8 Dwarka,Rs. 8553 - 9211,-,-
ncr,Sector-9 Dwarka,-,Rs. 16830 - 19635,Rs. 21760 - 24480
ncr,Sector-10 Dwarka,-,Rs. 16830 - 18700,Rs. 21760 - 24480
ncr,Sector-11 Dwarka,Rs. 9775 - 11050,Rs. 16830 - 19635,Rs. 23120 - 25840
ncr,Sector-12 Dwarka,-,Rs. 16830 - 18700,Rs. 22168 - 24939
ncr,Sector-13 Dwarka,Rs. 8925 - 11900,Rs. 14960 - 17765,Rs. 20400 - 25840
ncr,Sector-14 Dwarka,Rs. 9126 - 11614,-,-
ncr,Sector-15 Dwarka,-,-,-
ncr,Sector-16B Dwarka,Rs. 6885 - 8606,-,-
ncr,Sector-17 Dwarka,-,Rs. 14161 - 16660,-
ncr,Sector-18 Dwarka,Rs. 9157 - 10465,Rs. 16830 - 18700,Rs. 21038 - 23842
ncr,Sector-18A Dwarka,-,Rs. 18742 - 19784,Rs. 22440 - 23842
ncr,Sector-18B Dwarka,Rs. 8942 - 10283,Rs. 15300 - 17000,Rs. 20400 - 21760
ncr,Sector-19 Dwarka,Rs. 9466 - 12226,Rs. 15172 - 17850,Rs. 22440 - 23842
ncr,Sector-19B Dwarka,-,-,Rs. 21026 - 22340
ncr,Sector-22 Dwarka,-,Rs. 17340 - 20400,Rs. 20808 - 24970
ncr,Sector-23 Dwarka,Rs. 5780 - 7820,Rs. 16011 - 19778,Rs. 22168 - 23554
ncr,Sector-23B Dwarka,-,-,-
ncr,Sector-24 Dwarka,-,-,-
ncr,Adhchini,Rs. 12171 - 13816,-,-
ncr,Alaknanda,-,Rs. 23460 - 27540,Rs. 33150 - 39525
ncr,Ashram,-,-,-
ncr,Aya Nagar,-,Rs. 7721 - 10295,-
ncr,Chattarpur,Rs. 7480 - 7948,Rs. 11560 - 13005,Rs. 15640 - 16618
ncr,Chattarpur Enclave Phase 1,-,Rs. 11560 - 13005,-
ncr,Chattarpur Enclave Phase 2,Rs. 7012 - 7948,Rs. 10838 - 13005,Rs. 18238 - 20517
ncr,Chattarpur Extension,-,-,-
ncr,C R Park,-,Rs. 23868 - 26622,Rs. 34272 - 41616
ncr,Defence Colony,-,Rs. 43138 - 55038,-
ncr,Devli,-,-,-
ncr,East Of Kailash,-,Rs. 20482 - 24749,Rs. 35843 - 44804
ncr,Freedom Fighter Enclave,-,-,Rs. 19992 - 23990
ncr,Govind Puri,-,Rs. 14450 - 15895,-
ncr,Greater Kailash,Rs. 17106 - 22971,Rs. 35126 - 41182,Rs. 54128 - 67660
ncr,Greater Kailash I,-,Rs. 35153 - 46452,Rs. 46240 - 57800
ncr,Greater Kailash II,-,Rs. 36338 - 42394,-
ncr,Green Park,-,Rs. 34520 - 43814,-
ncr,Green Park Extension,-,-,-
ncr,Gulmohar Park,-,-,Rs. 56100 - 68000
ncr,Hauz Khas,-,-,Rs. 57443 - 72267
ncr,Jamia Nagar,-,-,-
ncr,Jangpura Extension,-,Rs. 22950 - 26775,Rs. 50575 - 54910
ncr,Jasola,Rs. 10200 - 11900,Rs. 15690 - 17932,Rs. 21420 - 23800
ncr,Kalkaji,Rs. 8032 - 9945,Rs. 16524 - 19278,-
ncr,Kalkaji Extension,-,Rs. 14790 - 16269,-
ncr,Khirki Extension,-,Rs. 16618 - 18785,-
ncr,Lajpat Nagar,Rs. 12437 - 16048,Rs. 20777 - 25230,-
ncr,Lajpat Nagar I,-,Rs. 20952 - 26010,-
ncr,Lajpat Nagar II,-,Rs. 21420 - 25245,-
ncr,Lajpat Nagar IV,-,Rs. 19125 - 24480,-
ncr,Mahipalpur,-,Rs. 9945 - 11271,-
ncr,Malviya Nagar,-,Rs. 20655 - 23715,Rs. 35493 - 45048
ncr,Munirka,Rs. 5797 - 6545,Rs. 24990 - 26775,Rs. 30345 - 34680
ncr,Neb Sarai,-,-,-
ncr,S.D.A,-,-,Rs. 56738 - 71868
ncr,Safdarjung,Rs. 21420 - 25245,Rs. 37591 - 41480,Rs. 50490 - 59670
ncr,Safdarjung Enclave,Rs. 21420 - 25245,Rs. 35126 - 39971,Rs. 50490 - 59670
ncr,Saket,-,Rs. 12750 - 17000,-
ncr,Sarita Vihar,-,Rs. 18572 - 21505,Rs. 22398 - 26350
ncr,Sector-B Vasant Kunj,-,Rs. 24083 - 27405,Rs. 34494 - 38326
ncr,Sector-C Vasant Kunj,-,-,Rs. 42840 - 56610
ncr,Sector-D Vasant Kunj,Rs. 15895 - 16830,Rs. 23536 - 26675,Rs. 34659 - 38818
ncr,Sheikh Sarai,-,-,-
ncr,Shivalik,-,-,Rs. 37868 - 47685
ncr,Sidharth Ext,-,-,-
ncr,South Extension,-,-,-
ncr,Sukhdev Vihar,-,-,-
ncr,Sultanpur,-,Rs. 11155 - 13780,-
ncr,Tughlakabad,-,-,-
ncr,Tughlakabad Extension,-,-,-
ncr,Vasant Kunj,Rs. 15428 - 16830,Rs. 24650 - 27200,Rs. 36720 - 42160
ncr,Vasant Vihar,Rs. 22399 - 30280,-,-
ncr,Ashok Vihar,-,Rs. 16437 - 19426,-
ncr,Burari,-,-,-
ncr,Keshav Puram,-,-,-
ncr,Loknayak Puram,-,-,-
ncr,Narela,-,-,-
ncr,Pitampura,Rs. 10285 - 13090,Rs. 12580 - 16354,Rs. 20400 - 24480
ncr,Prashant Vihar,-,-,-
ncr,Rohini,-,Rs. 14535 - 17595,Rs. 20757 - 25946
ncr,Sector-7 Rohini,-,-,-
ncr,Sector-8 Rohini,-,-,-
ncr,Sector-9 Rohini,-,Rs. 15682 - 18983,-
ncr,Sector-13 Rohini,Rs. 11050 - 12708,Rs. 15262 - 18475,Rs. 20893 - 24027
ncr,Sector-14 Rohini,-,-,Rs. 21795 - 28022
ncr,Sector-18 Rohini,-,Rs. 14605 - 16596,-
ncr,Sector-21 Rohini,-,-,-
ncr,Sector-22 Rohini,-,-,-
ncr,Sector-23 Rohini,-,-,-
ncr,Sector-24 Rohini,-,-,-
ncr,Sector-25 Rohini,-,-,-
ncr,Sector-28 Rohini,-,-,-
ncr,Sector-29 Rohini,-,-,-
ncr,Sector-34 Rohini,-,-,-
ncr,Shalimar Bagh,-,-,-
ncr,West Enclave,-,-,-
gurgaon,A Block Sushant Lok Phase - I,-,-,Rs. 59245 - 63985
gurgaon,Ardee City,-,-,Rs. 27961 - 34540
gurgaon,DLF CITY,-,-,Rs. 42500 - 52700
gurgaon,DLF CITY PHASE 1,-,Rs. 23588 - 29248,-
gurgaon,DLF CITY PHASE 2,-,-,Rs. 39015 - 46240
gurgaon,DLF CITY PHASE 3,-,-,-
gurgaon,DLF CITY PHASE 4,-,Rs. 27795 - 33354,Rs. 32465 - 37460
gurgaon,DLF CITY PHASE 5,-,Rs. 26350 - 29750,Rs. 31258 - 35889
gurgaon,Dwarka Expressway Gurgaon,Rs. 6864 - 9031,Rs. 9775 - 12708,Rs. 13821 - 17967
gurgaon,Golf Course Ext. Road,Rs. 11098 - 13709,Rs. 24480 - 28560,Rs. 29529 - 36091
gurgaon,Golf Course Road,-,Rs. 28511 - 33109,-
gurgaon,Gurgaon-Faridabad Road,-,-,-
gurgaon,Gwal Pahari,-,Rs. 14681 - 15545,Rs. 18488 - 20952
gurgaon,Heritage City,-,Rs. 34391 - 39304,-
gurgaon,IMT Manesar,-,-,-
gurgaon,Malibu Town,-,-,Rs. 23229 - 27584
gurgaon,MG Road,-,-,Rs. 38189 - 47002
gurgaon,New Gurgaon,-,Rs. 9775 - 11730,Rs. 13821 - 16585
gurgaon,NH-8,-,Rs. 11414 - 15218,Rs. 15166 - 19302
gurgaon,Nirvana Country,-,Rs. 23800 - 26180,Rs. 27200 - 32300
gurgaon,Palam Vihar,Rs. 16337 - 17391,Rs. 22270 - 23384,Rs. 27203 - 27203
gurgaon,Rampura,-,-,-
gurgaon,Rosewood,-,Rs. 21596 - 23196,Rs. 23375 - 26562
gurgaon,Sector-1 Imt Manesar,-,-,-
gurgaon,Sector-1A IMT Manesar,-,-,-
gurgaon,Sector-2 Gurgaon,-,Rs. 16524 - 17442,-
gurgaon,Sector-7 Gurgaon,-,-,-
gurgaon,Sector-15 Gurgaon,Rs. 12679 - 14600,Rs. 14450 - 19508,Rs. 22644 - 25160
gurgaon,Sector-22 Gurgaon,-,-,-
gurgaon,Sector-28 Gurgaon,Rs. 11732 - 12607,Rs. 28994 - 33826,Rs. 35924 - 44906
gurgaon,Sector-30 Gurgaon,-,-,Rs. 45268 - 50926
gurgaon,Sector-31 Gurgaon,-,-,Rs. 41954 - 45602
gurgaon,Sector-33 Gurgaon,-,Rs. 19242 - 22741,Rs. 21675 - 24225
gurgaon,Sector-37 Gurgaon,-,Rs. 10812 - 11893,Rs. 11498 - 14053
gurgaon,Sector-37C Gurgaon,-,Rs. 13260 - 14365,Rs. 12325 - 13558
gurgaon,Sector-37D Gurgaon,-,Rs. 10812 - 11893,Rs. 11498 - 14053
gurgaon,Sector-41 Gurgaon,-,Rs. 29555 - 33632,Rs. 35062 - 40672
gurgaon,Sector-42 Gurgaon,Rs. 15810 - 18445,-,Rs. 49613 - 60466
gurgaon,Sector-43 Gurgaon,-,Rs. 20840 - 26451,Rs. 31220 - 37166
gurgaon,Sector-45 Gurgaon,-,-,Rs. 22670 - 27203
gurgaon,Sector-46 Gurgaon,-,Rs. 16004 - 20449,Rs. 22766 - 27826
gurgaon,Sector-47 Gurgaon,-,Rs. 18625 - 20177,Rs. 29957 - 36615
gurgaon,Sector-48 Gurgaon,Rs. 27975 - 38784,Rs. 36285 - 43088,Rs. 30600 - 36720
gurgaon,Sector-49 Gurgaon,Rs. 11475 - 13540,Rs. 18700 - 23800,Rs. 27112 - 31630
gurgaon,Sector-50 Gurgaon,-,Rs. 23800 - 26180,Rs. 27200 - 32300
gurgaon,Sector-51 Gurgaon,-,-,Rs. 23906 - 30281
gurgaon,Sector-52 Gurgaon,Rs. 18785 - 20995,Rs. 25143 - 29478,-
gurgaon,Sector-53 Gurgaon,-,Rs. 33235 - 36168,Rs. 46002 - 54366
gurgaon,Sector-54 Gurgaon,-,-,Rs. 68813 - 87411
gurgaon,Sector-55 Gurgaon,-,-,Rs. 23800 - 28262
gurgaon,Sector-56 Gurgaon,Rs. 12258 - 13857,Rs. 18118 - 21569,Rs. 23800 - 26775
gurgaon,Sector-57 Gurgaon,-,Rs. 16796 - 20995,Rs. 28050 - 33660
gurgaon,Sector-58 Gurgaon,-,Rs. 33691 - 41177,Rs. 42500 - 45900
gurgaon,Sector-60 Gurgaon,-,Rs. 27907 - 31396,Rs. 30685 - 33915
gurgaon,Sector-61 Gurgaon,-,Rs. 24847 - 28988,Rs. 29878 - 33022
gurgaon,Sector-62 Gurgaon,-,-,Rs. 31195 - 35874
gurgaon,Sector-63 Gurgaon,-,Rs. 22603 - 23545,Rs. 27525 - 28835
gurgaon,Sector-63A Gurgaon,-,-,-
gurgaon,Sector-65 Gurgaon,-,Rs. 20862 - 22467,Rs. 47606 - 54407
gurgaon,Sector-66 Gurgaon,-,Rs. 26228 - 29974,Rs. 30719 - 36863
gurgaon,Sector-67 Gurgaon,-,Rs. 26392 - 28688,Rs. 30437 - 38046
gurgaon,Sector-69 Gurgaon,-,-,Rs. 20967 - 22200
gurgaon,Sector-70 Gurgaon,-,Rs. 20655 - 21802,Rs. 16766 - 21237
gurgaon,Sector-70A Gurgaon,-,Rs. 18523 - 20839,Rs. 21548 - 22984
gurgaon,Sector-71 Gurgaon,-,-,Rs. 17989 - 19373
gurgaon,Sector-72 Gurgaon,-,Rs. 23481 - 26244,Rs. 29117 - 32542
gurgaon,Sector-76 Gurgaon,-,-,-
gurgaon,Sector-77 Gurgaon,-,-,Rs. 14078 - 15161
gurgaon,Sector-78 Gurgaon,-,-,Rs. 12240 - 12240
gurgaon,Sector-80 Gurgaon,-,-,Rs. 15300 - 16830
gurgaon,Sector-81 Gurgaon,-,-,-
gurgaon,Sector-82 Gurgaon,-,Rs. 10149 - 12686,Rs. 13864 - 15250
gurgaon,Sector-82A Gurgaon,-,-,Rs. 24276 - 25704
gurgaon,Sector-83 Gurgaon,-,-,Rs. 15769 - 18397
gurgaon,Sector-84 Gurgaon,-,Rs. 10556 - 11516,Rs. 12928 - 14365
gurgaon,Sector-85 Gurgaon,-,Rs. 9050 - 12067,Rs. 10940 - 13370
gurgaon,Sector-88A Gurgaon,-,-,-
gurgaon,Sector-88B Gurgaon,-,-,-
gurgaon,Sector-89 A Gurgaon,-,-,-
gurgaon,Sector-89 Gurgaon,-,Rs. 7704 - 10271,Rs. 9520 - 10880
gurgaon,Sector-90 Gurgaon,-,-,Rs. 12370 - 16493
gurgaon,Sector-91 Gurgaon,-,-,Rs. 12294 - 12294
gurgaon,Sector-92 Gurgaon,-,Rs. 8288 - 9945,Rs. 9860 - 12325
gurgaon,Sector-93 Gurgaon,-,Rs. 10540 - 11594,Rs. 12355 - 13728
gurgaon,Sector-95 Gurgaon,-,-,-
gurgaon,Sector-95A Gurgaon,-,-,-
gurgaon,Sector-99A Gurgaon,-,-,-
gurgaon,Sector-102 Gurgaon,-,-,Rs. 14340 - 17207
gurgaon,Sector-103 Gurgaon,-,Rs. 8758 - 10948,Rs. 11206 - 12607
gurgaon,Sector-104 Gurgaon,-,Rs. 11220 - 13260,Rs. 14521 - 17161
gurgaon,Sector-107 Gurgaon,-,Rs. 11050 - 12155,Rs. 11791 - 14739
gurgaon,Sector-108 Gurgaon,-,Rs. 9180 - 12240,Rs. 13515 - 16218
gurgaon,Sector-109 Gurgaon,-,-,Rs. 14476 - 17371
gurgaon,Sector-110 A Gurgaon,-,Rs. 16524 - 18360,Rs. 20398 - 23536
gurgaon,Sector-110 Gurgaon,-,Rs. 16524 - 18360,Rs. 20398 - 23536
gurgaon,Sector-111 Gurgaon,-,-,Rs. 18255 - 21063
gurgaon,Sector-112 Gurgaon,-,-,-
gurgaon,Sector-113 Gurgaon,-,-,-
gurgaon,Sohna Road,-,Rs. 19224 - 23802,Rs. 27647 - 32255
gurgaon,South City,-,Rs. 28964 - 34956,Rs. 28274 - 39046
gurgaon,South City 1,-,Rs. 28372 - 34242,-
gurgaon,Southern Peripheral Road,-,Rs. 19508 - 20655,Rs. 18513 - 22216
gurgaon,Sun City,-,-,-
gurgaon,Sushant Lok,-,Rs. 20400 - 25296,Rs. 34558 - 38877
gurgaon,Sushant Lok Phase - 1,-,Rs. 20400 - 25296,Rs. 34558 - 38877
gurgaon,Sushant Lok Phase - 2,-,-,Rs. 21760 - 25840
gurgaon,Sushant Lok Phase - 3,-,Rs. 17578 - 23171,-
gurgaon,Vigyan Vihar,-,-,Rs. 20464 - 24556
noida,Arun Vihar,-,Rs. 12716 - 17484,Rs. 21458 - 22889
noida,Baraula,-,-,-
noida,Block C Sector-44 Noida,-,-,-
noida,Chhalera,-,-,-
noida,Hajipur,-,-,-
noida,Noida-Greater Noida Expressway,Rs. 10180 - 11585,Rs. 10078 - 11757,Rs. 13698 - 16188
noida,Noida Extension,Rs. 3481 - 3978,Rs. 5414 - 6962,Rs. 7562 - 8643
noida,Sector-16B Noida,-,-,-
noida,Sector-21 Noida,-,Rs. 12811 - 15213,Rs. 15658 - 18067
noida,Sector-25 Noida,-,Rs. 12138 - 14566,Rs. 19266 - 24771
noida,Sector-28 Noida,-,Rs. 20456 - 23865,Rs. 23120 - 26010
noida,Sector-29 Noida,Rs. 7242 - 8147,Rs. 14960 - 17765,Rs. 20260 - 24312
noida,Sector-30 Noida,-,-,Rs. 19762 - 21080
noida,Sector-34 Noida,Rs. 7018 - 9211,Rs. 15147 - 15988,Rs. 16891 - 17947
noida,Sector-37 Noida,-,Rs. 12920 - 16150,Rs. 22338 - 25316
noida,Sector-44 Noida,-,-,Rs. 26520 - 31492
noida,Sector-45 Noida,-,Rs. 14103 - 15866,Rs. 16575 - 19125
noida,Sector-46 Noida,-,Rs. 10948 - 12512,Rs. 13750 - 16041
noida,Sector-48 Noida,-,-,Rs. 17821 - 19441
noida,Sector-49 Noida,-,-,-
noida,Sector-50 Noida,-,Rs. 13438 - 15230,Rs. 17612 - 21386
noida,Sector-51 Noida,Rs. 9353 - 10690,Rs. 13120 - 15744,-
noida,Sector-52 Noida,Rs. 9125 - 11046,Rs. 13464 - 13464,Rs. 18177 - 19576
noida,Sector-53 Noida,-,Rs. 10276 - 11067,-
noida,Sector-61 Noida,-,Rs. 12277 - 14165,Rs. 17128 - 19762
noida,Sector-62 Noida,-,Rs. 11404 - 14035,Rs. 15300 - 17850
noida,Sector-70 Noida,-,Rs. 12125 - 12934,Rs. 13670 - 14912
noida,Sector-71 Noida,Rs. 7657 - 9571,-,-
noida,Sector-73 Noida,Rs. 4801 - 6001,-,-
noida,Sector-74 Noida,-,Rs. 12495 - 13388,-
noida,Sector-75 Noida,-,Rs. 10710 - 12495,Rs. 12665 - 16464
noida,Sector-76 Noida,-,Rs. 10231 - 11936,Rs. 12070 - 13277
noida,Sector-77 Noida,Rs. 7946 - 8364,Rs. 11216 - 13804,Rs. 14754 - 17437
noida,Sector-78 Noida,Rs. 7925 - 10127,Rs. 11337 - 13082,Rs. 11900 - 15470
noida,Sector-79 Noida,-,-,-
noida,Sector-82 Noida,Rs. 6962 - 8354,Rs. 9331 - 10180,Rs. 10159 - 11288
noida,Sector-92 Noida,-,-,-
noida,Sector-93 B Noida,-,Rs. 13388 - 15172,Rs. 20145 - 22831
noida,Sector-93 Noida,-,Rs. 11768 - 14484,Rs. 16779 - 22372
noida,Sector-94 Noida,-,-,-
noida,Sector-99 Noida,-,-,Rs. 14918 - 17901
noida,Sector-100 Noida,-,Rs. 13348 - 15402,Rs. 16830 - 18232
noida,Sector-104 Noida,-,-,Rs. 28626 - 31807
noida,Sector-107 Noida,-,Rs. 14025 - 14960,Rs. 17360 - 18695
noida,Sector-108 Noida,-,-,-
noida,Sector-110 Noida,-,Rs. 10781 - 12578,Rs. 13922 - 15188
noida,Sector-117 Noida,-,Rs. 5760 - 7041,Rs. 6969 - 7744
noida,Sector-118 Noida,-,-,-
noida,Sector-119 Noida,-,Rs. 9750 - 10724,Rs. 10452 - 13064
noida,Sector-120 Noida,Rs. 8124 - 8576,Rs. 9266 - 10108,Rs. 10167 - 12426
noida,Sector-121 Noida,-,Rs. 9476 - 11055,Rs. 19938 - 22430
noida,Sector-128 Noida,Rs. 12282 - 15172,Rs. 12515 - 15644,Rs. 24089 - 27795
noida,Sector-129 Noida,-,-,Rs. 11518 - 13821
noida,Sector-132 Noida,-,-,-
noida,Sector-133 Noida,-,-,-
noida,Sector-134 Noida,-,Rs. 7166 - 8599,Rs. 9272 - 11332
noida,Sector-135 Noida,-,Rs. 9935 - 10763,Rs. 11543 - 15006
noida,Sector-137 Noida,Rs. 10532 - 11585,Rs. 10027 - 11698,Rs. 12180 - 14617
noida,Sector-143 Noida,-,Rs. 8415 - 10098,Rs. 12688 - 12688
noida,Sector-143B Noida,-,-,Rs. 11475 - 14025
noida,Sector-144 Noida,-,-,-
noida,Sector-150 Noida,-,-,Rs. 16473 - 21415
noida,Sector-151 Noida,-,Rs. 6212 - 7592,Rs. 10106 - 11117
noida,Sector-152 Noida,-,-,-
noida,Sector-168 Noida,-,-,Rs. 11160 - 12277
noida,Alpha-I Gr Noida,-,Rs. 9818 - 10710,Rs. 10894 - 12104
noida,Alpha-II Gr Noida,-,Rs. 9086 - 9995,-
noida,Eta II,-,-,-
noida,Greater Noida West,-,Rs. 6297 - 7084,Rs. 7794 - 8908
noida,Gurjinder Vihar,-,-,Rs. 7744 - 9292
noida,Jaypee Greens,-,Rs. 13404 - 17426,Rs. 19635 - 26775
noida,Omega II  Gr Noida,-,-,Rs. 9343 - 11679
noida,Pari Chowk,-,Rs. 7480 - 9350,Rs. 9520 - 10880
noida,Sector-2 Gr Noida,-,Rs. 5629 - 7237,Rs. 6783 - 9044
noida,Sector-4 Gr Noida,-,Rs. 7459 - 8288,Rs. 7878 - 9003
noida,Sector-10 Greater Noida West,-,-,-
noida,Sector-16 B Gr Noida,-,-,Rs. 7824 - 10060
noida,Sector-16 Gr Noida,-,-,Rs. 7229 - 8262
noida,Sector-16C Greater Noida,-,Rs. 6358 - 7948,Rs. 8031 - 9035
noida,Sector-Pi Gr Noida,-,Rs. 8044 - 11061,Rs. 10826 - 12179
noida,Sector 1 Greater Noida West,Rs. 4675 - 5610,Rs. 5712 - 7344,Rs. 8021 - 9166
noida,Sector 17A,-,-,-
noida,Sector Chi-2 Greater Noida,-,-,-
noida,Sector Chi 3 Gr Noida,-,-,Rs. 10407 - 11893
noida,Sector Chi 4 Gr Noida,-,-,Rs. 10921 - 13651
noida,Sector Chi 5 Gr Noida,-,-,-
noida,Sector Chi Gr Noida,-,-,-
noida,Sector MU 2 Greater Noida,-,-,-
noida,Sector Mu Gr Noida,-,-,-
noida,Sector Omega -1 Gr Noida,-,-,-
noida,Sector Omicron 1A Greater Noida,-,-,-
noida,Sector Omicron I Greater Noida,Rs. 7381 - 8546,Rs. 6460 - 8075,-
noida,Sector Omicron III Greater Noida,-,Rs. 6936 - 7803,Rs. 10073 - 11512
noida,Sector Phi  Gr Noida,-,Rs. 7948 - 8670,-
noida,Sector Phi IV Greater Noida,-,Rs. 6842 - 6842,-
noida,Sector Phi Ll Gr Noida,-,Rs. 7948 - 8670,-
noida,Sector Pi- 1 Gr Noida,-,Rs. 8687 - 11293,Rs. 10479 - 11789
noida,Sector Pi- II Gr Noida,-,Rs. 8500 - 11688,Rs. 9532 - 12255
noida,Sector ZETA Gr Noida,Rs. 4930 - 4930,Rs. 7140 - 8925,Rs. 11475 - 12750
noida,Sector ZETA I Gr Noida,Rs. 4930 - 4930,Rs. 7133 - 8916,Rs. 11475 - 12750
noida,Shahberi,-,-,-
noida,Sigma IV,-,-,-
noida,Site C Gr Noida,-,Rs. 6249 - 7812,-
noida,Surajpur,-,-,-
noida,Swaran Nagri,-,-,Rs. 11900 - 13600
noida,Techzone,-,Rs. 5916 - 7395,Rs. 8568 - 11016
noida,Techzone 4 Greater Noida West,-,Rs. 5916 - 7395,Rs. 8568 - 11016
noida,Yamuna Expressway,-,-,-
ghaziabad,Abhay Khand,-,Rs. 9894 - 12862,-
ghaziabad,Abhay Khand 3,-,-,-
ghaziabad,Ahinsa Khand,-,Rs. 11230 - 14038,-
ghaziabad,Ahinsa Khand 1,-,Rs. 12155 - 14960,Rs. 18232 - 21038
ghaziabad,Ahinsa Khand 2,-,Rs. 10752 - 12708,Rs. 11827 - 13141
ghaziabad,Ankur Vihar,-,-,-
ghaziabad,Bamheta,-,Rs. 4427 - 5692,-
ghaziabad,Bhopura,-,-,-
ghaziabad,Crossing Republik,-,Rs. 6521 - 7453,Rs. 7905 - 9222
ghaziabad,Dasna,-,-,-
ghaziabad,Dundahera,-,-,-
ghaziabad,Gyan Khand,-,-,-
ghaziabad,Gyan Khand 3,-,-,-
ghaziabad,Indirapuram,-,Rs. 11016 - 13770,Rs. 14680 - 17348
ghaziabad,Judges Enclave,-,Rs. 10238 - 11169,Rs. 11475 - 12750
ghaziabad,Kaushambi,-,Rs. 11526 - 12294,-
ghaziabad,Kinauni Village,-,-,-
ghaziabad,Lajpat Nagar - Ghaziabad,-,-,-
ghaziabad,Lal Kuan,-,Rs. 4992 - 5705,-
ghaziabad,Loni,-,-,-
ghaziabad,Madhuban Bapudham,-,-,-
ghaziabad,Mehrauli,-,Rs. 5562 - 6258,Rs. 6224 - 7113
ghaziabad,Mohan Nagar,-,-,Rs. 10710 - 11900
ghaziabad,N.H-58,-,-,-
ghaziabad,NH-24 Highway,-,Rs. 5807 - 6533,Rs. 7820 - 7820
ghaziabad,NH 91,-,Rs. 4992 - 5705,-
ghaziabad,Niti Khand,-,-,-
ghaziabad,Nyay Khand 1,-,Rs. 11149 - 13007,-
ghaziabad,Nyay Khand 2,-,Rs. 9119 - 9879,-
ghaziabad,Nyay Khand III,-,-,-
ghaziabad,Pratap Vihar,-,-,-
ghaziabad,Rajendar Nagar,-,Rs. 6120 - 7650,-
ghaziabad,Raj Nagar Extension,-,Rs. 6059 - 7574,Rs. 7140 - 9180
ghaziabad,Ramprastha,-,-,-
ghaziabad,Ramprastha Greens,-,Rs. 14606 - 16432,Rs. 19172 - 22121
ghaziabad,Sahibabad,-,-,-
ghaziabad,Sanjay Nagar,-,-,-
ghaziabad,Sector-1 Vaishali,Rs. 9889 - 10360,Rs. 11696 - 12427,Rs. 14078 - 17326
ghaziabad,Sector-1 Vasundhara,-,-,-
ghaziabad,Sector-2 Vaishali,-,-,-
ghaziabad,Sector-3 Vaishali,-,Rs. 13388 - 14280,Rs. 16575 - 19125
ghaziabad,Sector-3 Vasundhara,-,Rs. 9843 - 11812,-
ghaziabad,Sector-4 Vaishali,-,Rs. 12750 - 13600,Rs. 15198 - 17731
ghaziabad,Sector-4C Vasundhara,-,-,-
ghaziabad,Sector-5 Vaishali,Rs. 6341 - 7292,Rs. 12417 - 13193,Rs. 15586 - 19837
ghaziabad,Sector-5 Vasundhara,-,-,Rs. 13812 - 17956
ghaziabad,Sector-7 Vaishali,-,-,Rs. 17626 - 19094
ghaziabad,Sector-9 Vaishali,-,Rs. 11233 - 13479,Rs. 17207 - 18641
ghaziabad,Sector 9 Vasundhara,-,-,-
ghaziabad,Shakti Khand,-,-,-
ghaziabad,Shalimar Garden,Rs. 4675 - 5100,Rs. 6800 - 7650,-
ghaziabad,Shalimar Garden Extension I,-,Rs. 6827 - 8534,-
ghaziabad,Shalimar Garden Extension II,-,Rs. 6732 - 7480,-
ghaziabad,Siddhartha Vihar,Rs. 4376 - 5105,-,-
ghaziabad,Surya Nagar,-,-,-
ghaziabad,Vaibhav Khand,-,Rs. 11602 - 12495,Rs. 14848 - 17547
ghaziabad,Vaishali,Rs. 8476 - 9889,Rs. 12750 - 14450,Rs. 16320 - 19040
ghaziabad,Vasundhara,-,Rs. 10618 - 12388,Rs. 13600 - 17680
ghaziabad,Vijay Nagar,-,-,-
ghaziabad,Wave City,-,-,-
faridabad,Charmwood Village,-,Rs. 20738 - 22624,Rs. 20494 - 23730
faridabad,Nehar Par,-,Rs. 8453 - 10332,Rs. 11858 - 13175
faridabad,Sector 21C Faridabad,-,-,Rs. 12538 - 15045
faridabad,Sector 21D Faridabad,-,-,Rs. 13903 - 15167
faridabad,Sector 39 Faridabad,-,Rs. 20738 - 22624,Rs. 20494 - 23730
faridabad,Sector 43 Faridabad,-,-,Rs. 21864 - 21864
faridabad,Sector 45 Faridabad,-,-,-
faridabad,Sector 46 Faridabad,-,-,Rs. 11994 - 13193
faridabad,Sector 48 Faridabad,-,-,-
faridabad,Sector 70 Faridabad,-,Rs. 7317 - 9146,Rs. 10060 - 11178
faridabad,Sector 75 Faridabad,-,-,Rs. 10603 - 12118
faridabad,Sector 76 Faridabad,-,-,-
faridabad,Sector 77 Faridabad,-,Rs. 5829 - 6801,Rs. 7650 - 8925
faridabad,Sector 78 Faridabad,-,-,Rs. 9554 - 10748
faridabad,Sector 79 Faridabad,-,-,-
faridabad,Sector 80 Faridabad,-,-,-
faridabad,Sector 81 Faridabad,-,-,-
faridabad,Sector 82 Faridabad,-,-,Rs. 15564 - 17120
faridabad,Sector 84 Faridabad,-,-,Rs. 9371 - 12495
faridabad,Sector 85 Faridabad,-,-,-
faridabad,Sector 86 Faridabad,-,Rs. 9350 - 12155,Rs. 11475 - 14025
faridabad,Sector 87 Faridabad,-,-,Rs. 10710 - 10710
faridabad,Sector 88 Faridabad,-,Rs. 9096 - 10106,Rs. 12240 - 12240
faridabad,Sector 89 Faridabad,-,Rs. 6872 - 7854,Rs. 8544 - 8544
faridabad,Suraj Kund,-,-,-
mumbai,Anand Nagar,Rs. 10811 - 11751,Rs. 17000 - 18700,-
mumbai,Balkum,Rs. 10353 - 13459,-,-
mumbai,Brahmand,Rs. 11016 - 11934,Rs. 15172 - 17340,-
mumbai,Budhaji Nagar,Rs. 8925 - 11602,-,-
mumbai,Charai,-,Rs. 20655 - 25474,-
mumbai,Dhobi Ali,-,-,-
mumbai,Dhokali,Rs. 12750 - 14280,Rs. 17536 - 20586,Rs. 20107 - 26456
mumbai,Diva Gaon,-,-,-
mumbai,Dokali Pada,-,Rs. 17497 - 21301,-
mumbai,Gawand Baug,-,-,-
mumbai,G B Road,-,-,-
mumbai,Ghodbunder Road,Rs. 11613 - 14642,Rs. 16833 - 20840,Rs. 25787 - 31648
mumbai,Hiranandani Estate,Rs. 15810 - 17340,Rs. 21619 - 24021,Rs. 30451 - 34105
mumbai,Hiranandani Meadows,-,Rs. 25474 - 28022,Rs. 33048 - 37944
mumbai,Kailash Nagar,-,-,-
mumbai,Kalher,-,-,-
mumbai,Kalwa,Rs. 10540 - 12121,Rs. 13424 - 15793,-
mumbai,Kapurbawadi,Rs. 13685 - 15327,Rs. 19380 - 21802,Rs. 25112 - 31390
mumbai,Kasar Vadavali,Rs. 9775 - 11241,Rs. 13421 - 15540,Rs. 18727 - 21848
mumbai,Kasheli,-,-,-
mumbai,Kavesar,Rs. 11832 - 12818,Rs. 18289 - 19951,Rs. 22950 - 26392
mumbai,Khopat,Rs. 14864 - 16402,Rs. 20196 - 23188,-
mumbai,Kolshet Industrial Area,-,-,Rs. 18360 - 22440
mumbai,Kolshet Road,Rs. 13294 - 14450,Rs. 16779 - 17578,Rs. 21250 - 25500
mumbai,Kopri,-,Rs. 22610 - 24225,-
mumbai,Laxmi Nagar,-,-,-
mumbai,Louis Wadi,Rs. 13570 - 17510,-,-
mumbai,Majiwada,Rs. 13426 - 16906,Rs. 19859 - 22568,Rs. 25585 - 29423
mumbai,Manisha Nagar,Rs. 8693 - 11177,-,-
mumbai,Manpada,Rs. 14174 - 15151,Rs. 21229 - 23776,Rs. 25245 - 29835
mumbai,Naupada,Rs. 16320 - 18360,Rs. 26086 - 31136,-
mumbai,Owale,Rs. 8476 - 10360,Rs. 11603 - 15016,-
mumbai,Panch Pakhadi,Rs. 16266 - 18299,Rs. 22610 - 26648,-
mumbai,Parsik Nagar,Rs. 10710 - 11246,Rs. 13728 - 16150,-
mumbai,Patlipada,Rs. 12852 - 15708,Rs. 18062 - 20952,Rs. 29504 - 32908
mumbai,Pokharan Road,-,Rs. 18514 - 22539,-
mumbai,Pokhran-2,Rs. 14356 - 15792,Rs. 21038 - 25245,Rs. 28050 - 31556
mumbai,Sai Nagar,Rs. 10622 - 13036,Rs. 13114 - 14494,-
mumbai,Sainath Nagar,Rs. 14756 - 16660,Rs. 20591 - 23062,Rs. 28050 - 31875
mumbai,Samata Nagar,Rs. 15664 - 17046,Rs. 23460 - 25806,Rs. 28846 - 31936
mumbai,Shree Nagar,-,-,-
mumbai,Teen Haath Naka,Rs. 14178 - 16541,Rs. 23689 - 25217,Rs. 42595 - 43926
mumbai,Thane (East),Rs. 14144 - 15912,Rs. 20230 - 24565,-
mumbai,Thane West,Rs. 11437 - 14918,Rs. 17634 - 21642,Rs. 25245 - 30982
mumbai,Uthalsar,-,-,-
mumbai,Vartak Nagar,Rs. 14535 - 15020,Rs. 17660 - 18921,-
mumbai,Vasant Vihar,Rs. 13948 - 15808,Rs. 22015 - 24374,Rs. 25542 - 28608
mumbai,Vijay Nagari,Rs. 10772 - 12645,Rs. 16830 - 19125,-
mumbai,Vitawa,-,-,-
mumbai,Waghbil,Rs. 11144 - 12597,Rs. 14793 - 17908,-
mumbai,Wagle Estate,Rs. 14282 - 16585,-,-
mumbai,Adharwadi,Rs. 5142 - 6078,Rs. 7268 - 8882,-
mumbai,Ambernath,Rs. 4141 - 5176,Rs. 5868 - 7336,-
mumbai,Ambernath East,-,Rs. 6351 - 8733,-
mumbai,Ambernath West,Rs. 4114 - 5142,Rs. 6502 - 7225,-
mumbai,Ambivli,Rs. 2601 - 3468,-,-
mumbai,Amrut Nagar,Rs. 22908 - 26180,-,-
mumbai,Anand Nagar,-,-,-
mumbai,Anjurdive,-,-,-
mumbai,Asangaon,-,-,-
mumbai,Atgaon,-,-,-
mumbai,Badlapur,Rs. 3528 - 4032,Rs. 4360 - 5814,-
mumbai,Badlapur (East),Rs. 2830 - 3774,Rs. 5022 - 5739,-
mumbai,Badlapur (West),Rs. 3131 - 4175,Rs. 4529 - 6038,-
mumbai,Belavali,Rs. 3213 - 4284,-,-
mumbai,Bhivpuri,-,-,-
mumbai,Bhiwandi,Rs. 4483 - 5479,Rs. 8181 - 9669,-
mumbai,Bhoiwada,-,Rs. 62397 - 70448,Rs. 91910 - 100266
mumbai,Chanakya Nagar,-,-,-
mumbai,Chikan Ghar,-,Rs. 11900 - 13600,-
mumbai,Chikholi,Rs. 3820 - 4366,-,-
mumbai,Desale Pada,-,-,-
mumbai,Devicha Pada,-,-,-
mumbai,Diva,Rs. 3699 - 5086,-,-
mumbai,Dombivli (East),Rs. 6365 - 7834,Rs. 9381 - 10825,Rs. 10266 - 13066
mumbai,Dombivli (West),-,Rs. 7684 - 9989,-
mumbai,Gandhar Nagar,Rs. 7140 - 8160,Rs. 10498 - 12112,-
mumbai,Gauripada,-,-,-
mumbai,Gograswadi,-,-,-
mumbai,Hendre Pada,-,-,-
mumbai,Jadhav Colony,-,-,-
mumbai,Joveli Gaon,-,-,-
mumbai,Kalu Nagar,-,-,-
mumbai,Kalwa,-,-,-
mumbai,Kalyan (East),-,-,-
mumbai,Kalyan (West),Rs. 6630 - 7650,Rs. 10663 - 12304,-
mumbai,Karjat,-,-,-
mumbai,Katemanivali,-,-,-
mumbai,Katrap,Rs. 3213 - 4284,Rs. 5319 - 6079,-
mumbai,Khadakpada,Rs. 6630 - 7650,Rs. 10575 - 12202,-
mumbai,Kharegaon,Rs. 9775 - 10752,-,-
mumbai,Kharvai,Rs. 2805 - 3272,-,-
mumbai,Khatiwali,-,-,-
mumbai,Khoni,-,-,-
mumbai,Khopoli,Rs. 4437 - 5423,-,-
mumbai,Kopargaon,-,-,-
mumbai,Kulgaon,Rs. 3570 - 4080,-,-
mumbai,Manda,Rs. 3835 - 4794,-,-
mumbai,Manjarli,Rs. 3213 - 4284,-,-
mumbai,Morivali,-,-,-
mumbai,Mumbra,-,-,-
mumbai,Nandivali Panchanand,-,-,-
mumbai,Nandivli,-,-,-
mumbai,Neral,-,-,-
mumbai,Nilje Gaon,Rs. 7012 - 7480,Rs. 9238 - 9948,Rs. 10302 - 11160
mumbai,Pandurangwadi,-,-,-
mumbai,Pendse Nagar,-,-,-
mumbai,Radha Nagar,-,-,-
mumbai,Rambaug,-,-,-
mumbai,Rameshwadi,-,-,-
mumbai,Sagaon,-,-,-
mumbai,Sangeeta Wadi,-,-,-
mumbai,Shahad,-,-,-
mumbai,Shahpur,-,-,-
mumbai,Shastri Nagar,-,-,-
mumbai,Shirgaon,Rs. 3510 - 4012,Rs. 5034 - 5753,-
mumbai,Sunil Nagar,-,-,-
mumbai,Thakurli,Rs. 6630 - 7650,-,-
mumbai,Tilak Nagar,-,-,-
mumbai,Titwala,Rs. 3951 - 4938,Rs. 6256 - 7038,-
mumbai,Ulhasnagar,-,-,-
mumbai,Umesh Nagar,-,-,-
mumbai,Valivali Gaon,-,-,-
mumbai,Vangani,Rs. 2570 - 2999,-,-
mumbai,Vasind,Rs. 2720 - 3060,-,-
mumbai,Vishnunagar,-,-,-
mumbai,Wayale Nagar,-,-,-
mumbai,Wayle Nagar,Rs. 6763 - 8323,Rs. 10498 - 12112,-
mumbai,Yogidham,Rs. 6818 - 8391,-,-
mumbai,Agashi,-,-,-
mumbai,Ambawadi,-,-,-
mumbai,Bevarly Park,Rs. 9818 - 10752,Rs. 13243 - 15334,-
mumbai,Bhayander (East),Rs. 9282 - 11050,Rs. 12971 - 14268,-
mumbai,Bhayander (West),-,-,-
mumbai,Boisar,-,-,-
mumbai,Bolinj,-,-,-
mumbai,Chandan Shanti,-,-,-
mumbai,Chikhal Dongari,Rs. 4530 - 5890,Rs. 5539 - 7385,-
mumbai,Dongarpada,-,-,-
mumbai,Geeta Nagar,-,-,-
mumbai,Ghodev,-,-,-
mumbai,Gokul Township,-,-,-
mumbai,Hatkesh Udhog Nagar,Rs. 9139 - 10445,Rs. 12179 - 13532,-
mumbai,Jesal Park,-,-,-
mumbai,Juchandra,-,-,-
mumbai,Kanakia Park,Rs. 8925 - 10710,Rs. 13296 - 16989,-
mumbai,Kashimira,-,Rs. 11465 - 13614,-
mumbai,Lakshmiben Chedda Nagar,-,-,-
mumbai,Medetiya Nagar,-,-,-
mumbai,Mira Bhayandar,Rs. 10192 - 11581,Rs. 14110 - 16226,Rs. 18700 - 21505
mumbai,Mira Road,Rs. 9818 - 11220,Rs. 13906 - 15992,Rs. 17813 - 20626
mumbai,Mira Road East,Rs. 9782 - 11645,Rs. 13485 - 16324,Rs. 19125 - 21994
mumbai,Morya Nagar,Rs. 4122 - 4947,Rs. 5432 - 6035,-
mumbai,Naigaon (East),Rs. 4254 - 5028,-,-
mumbai,Naigaon (West),Rs. 4122 - 4947,Rs. 5432 - 6035,-
mumbai,Nalasopara (West),Rs. 4122 - 4535,Rs. 5470 - 6685,-
mumbai,Nalasopara East,Rs. 4122 - 4947,Rs. 5699 - 6966,-
mumbai,Nallasopara,Rs. 4122 - 4947,Rs. 5584 - 6826,-
mumbai,Navghar Gaon,-,-,-
mumbai,Nilemore,Rs. 4122 - 4947,Rs. 5508 - 6120,-
mumbai,Poonam Gardens,-,-,-
mumbai,Poonam Nagar,-,-,-
mumbai,Poonam Sagar Complex,-,-,-
mumbai,Ramdev Park,-,-,-
mumbai,Shanti Nagar,-,-,-
mumbai,Shanti Park,-,-,-
mumbai,Sheetal Nagar,-,-,-
mumbai,Sriprastha,-,-,-
mumbai,Vasai,Rs. 6210 - 7166,Rs. 8170 - 9532,-
mumbai,Vasai East,Rs. 6210 - 7166,Rs. 8170 - 9532,-
mumbai,Vasai Road,-,-,-
mumbai,Vasai West,Rs. 6464 - 7459,Rs. 8895 - 9580,-
mumbai,Vasant Nagari,-,-,-
mumbai,Vijay Park,-,-,-
mumbai,Vinay Nagar,-,-,-
mumbai,Virar,Rs. 4684 - 5620,Rs. 6044 - 7386,Rs. 6916 - 8644
mumbai,Virar East,Rs. 3995 - 5194,-,-
mumbai,Virar West,Rs. 4684 - 5620,Rs. 6044 - 7386,Rs. 6916 - 8644
mumbai,Y K Nagar,-,-,-
mumbai,4 Bunglows,Rs. 24225 - 31025,Rs. 43350 - 48450,Rs. 53780 - 59755
mumbai,Aarey Milk Colony,Rs. 16371 - 20464,Rs. 21216 - 23338,Rs. 23899 - 29330
mumbai,Akurli Nagar,-,-,-
mumbai,Alika Nagar,-,-,-
mumbai,Ambivali,-,-,-
mumbai,Amboli,Rs. 21038 - 22185,Rs. 36902 - 43680,-
mumbai,Anand Nagar,-,Rs. 43605 - 45220,Rs. 96968 - 105453
mumbai,Andheri (East),Rs. 23842 - 27115,Rs. 36832 - 42437,Rs. 50517 - 59303
mumbai,Andheri (West),Rs. 22440 - 28985,Rs. 36834 - 46238,Rs. 58393 - 73885
mumbai,Andheri MIDC,Rs. 14280 - 17850,-,-
mumbai,Asara Colony,-,-,-
mumbai,Asha Nagar,Rs. 16940 - 19111,Rs. 23264 - 25923,Rs. 30573 - 35350
mumbai,Azad Nagar,Rs. 22366 - 26474,Rs. 38312 - 42388,Rs. 53984 - 62772
mumbai,Babhai,-,-,-
mumbai,Bangur Nagar,Rs. 17738 - 21573,Rs. 30842 - 34604,-
mumbai,Bhagat Colony,-,-,-
mumbai,Borivali (East),Rs. 14941 - 18017,Rs. 26086 - 30039,Rs. 38208 - 44370
mumbai,Borivali (West),Rs. 15262 - 18314,Rs. 23113 - 28016,Rs. 34193 - 37301
mumbai,Cama Industrial Estate,-,-,-
mumbai,Chakala,Rs. 16565 - 18635,Rs. 39100 - 46138,-
mumbai,Charkop,Rs. 15895 - 17298,Rs. 20301 - 22477,-
mumbai,Chikuwadi,Rs. 15667 - 18278,-,-
mumbai,Chincholi Bunder,Rs. 21408 - 24030,Rs. 26596 - 29763,-
mumbai,Churi Wadi,-,-,-
mumbai,Dahanukar Wadi,-,-,-
mumbai,Dahisar,Rs. 13064 - 14866,Rs. 17468 - 20961,Rs. 25296 - 26350
mumbai,Dahisar (East),Rs. 12566 - 13913,Rs. 16606 - 19373,Rs. 25255 - 26308
mumbai,Dahisar (West),Rs. 14866 - 16218,Rs. 21675 - 24565,-
mumbai,Dattaguru Nagar,-,Rs. 40759 - 45005,-
mumbai,Dattapada,-,-,-
mumbai,Daulat Nagar,-,-,-
mumbai,Devipada,-,-,-
mumbai,Dindoshi,Rs. 19354 - 21879,Rs. 27455 - 33235,Rs. 49966 - 54509
mumbai,DN Nagar,-,Rs. 36125 - 43350,Rs. 54835 - 71808
mumbai,Eksar,-,-,-
mumbai,Ekta Nagar,Rs. 12342 - 14212,-,-
mumbai,Evershine Nagar,Rs. 15580 - 17978,Rs. 29070 - 31492,-
mumbai,Film City Road,Rs. 20918 - 23192,Rs. 33017 - 37250,Rs. 39419 - 43924
mumbai,Gokuldham,Rs. 19125 - 21250,Rs. 36168 - 40078,Rs. 53491 - 59975
mumbai,Gorai,-,-,-
mumbai,Goregaon (East),Rs. 19518 - 22695,Rs. 33150 - 38250,Rs. 62135 - 73695
mumbai,Goregaon (West),Rs. 20102 - 23842,Rs. 32094 - 36679,Rs. 48319 - 56185
mumbai,Hanuman Nagar,-,-,-
mumbai,Hemu Colony,-,-,-
mumbai,I C Colony,Rs. 14198 - 15973,Rs. 23399 - 25663,-
mumbai,Irani Wadi,-,-,-
mumbai,Jankalyan Nagar,Rs. 16541 - 18431,Rs. 22924 - 25981,-
mumbai,Jawahar Nagar,Rs. 16906 - 21675,Rs. 26732 - 30345,-
mumbai,Jay Prakash Nagar,Rs. 18700 - 21505,Rs. 27455 - 31068,-
mumbai,J B Nagar,Rs. 24544 - 26775,Rs. 37952 - 44412,-
mumbai,Jogeshwari (East),Rs. 22908 - 26648,Rs. 39950 - 44200,Rs. 58851 - 65390
mumbai,Jogeshwari (West),Rs. 20102 - 22440,Rs. 32300 - 41182,-
mumbai,JVLR,Rs. 21926 - 24318,Rs. 39950 - 45050,-
mumbai,Kajupada,-,-,-
mumbai,Kanchpada,Rs. 21802 - 27616,-,-
mumbai,Kandarpada,Rs. 13954 - 14826,Rs. 20018 - 22686,-
mumbai,Kandivali (East),Rs. 16376 - 18962,-,-
mumbai,Kandivali (West),Rs. 15976 - 18714,Rs. 21981 - 25644,Rs. 38097 - 42330
mumbai,Kasam Baug,-,Rs. 34850 - 39950,-
mumbai,Ketkipada,-,-,-
mumbai,Liberty Garden,Rs. 16150 - 18700,-,-
mumbai,Link Road,-,Rs. 30600 - 35955,-
mumbai,Lokhandwala Andheri West,-,-,Rs. 67788 - 75182
mumbai,Lokhandwala Kandivali East,Rs. 15159 - 17207,Rs. 24216 - 26559,Rs. 27514 - 29631
mumbai,Madh,-,-,-
mumbai,Mahakali Caves,Rs. 25727 - 27984,Rs. 32360 - 36674,-
mumbai,Maharashtra Nagar,Rs. 18476 - 20420,-,-
mumbai,Mahavir Nagar,Rs. 19168 - 21038,Rs. 28530 - 31791,-
mumbai,Malad (East),Rs. 18742 - 22312,Rs. 32776 - 36873,Rs. 46294 - 51299
mumbai,Malad (West),Rs. 17404 - 21420,Rs. 28305 - 33660,Rs. 41703 - 49188
mumbai,Malvani,Rs. 13780 - 17225,Rs. 19508 - 24565,-
mumbai,Marol,Rs. 24098 - 27471,Rs. 35904 - 41616,Rs. 44200 - 53040
mumbai,Maruti Nagar,Rs. 13977 - 15422,-,-
mumbai,Mhatre Wadi,-,-,-
mumbai,Mindspace,Rs. 21588 - 24128,Rs. 34745 - 41851,Rs. 48875 - 52062
mumbai,Mitha Nagar,Rs. 22908 - 25245,-,-
mumbai,Motilal Nagar II,Rs. 23491 - 24929,Rs. 29223 - 35717,-
mumbai,Natwar Nagar,-,-,-
mumbai,Nensey Colony,Rs. 13597 - 15790,-,-
mumbai,Orlem,Rs. 19242 - 21075,Rs. 25823 - 31725,-
mumbai,Oshiwara,Rs. 23460 - 29814,Rs. 35955 - 39780,-
mumbai,Prem Nagar,Rs. 8055 - 9914,-,-
mumbai,Pushpa Park,-,-,-
mumbai,Rawalpada,Rs. 12376 - 13702,-,-
mumbai,Safed Pul,-,Rs. 36465 - 43010,Rs. 56330 - 58726
mumbai,Sahayog Nagar,-,-,Rs. 53550 - 55930
mumbai,Saibaba Nagar,Rs. 15351 - 17105,-,-
mumbai,Sakinaka,Rs. 26648 - 30378,Rs. 37101 - 41317,Rs. 48659 - 55610
mumbai,Samta Nagar,-,Rs. 17304 - 21481,-
mumbai,Sankalp Colony,-,-,-
mumbai,Satya Nagar,-,Rs. 27068 - 30349,-
mumbai,Sector-8 Charkop,Rs. 16097 - 17991,Rs. 21026 - 23202,-
mumbai,Sector-9 Charkop,-,-,-
mumbai,Sector 1 Charkop,-,-,-
mumbai,Sector 2 Charkop,-,Rs. 18945 - 20975,-
mumbai,Sector 3 Charkop,Rs. 16571 - 18465,-,-
mumbai,Seven Bunglow,-,-,Rs. 56695 - 69020
mumbai,Shastri Nagar,Rs. 33724 - 38122,Rs. 46890 - 52454,Rs. 67215 - 86238
mumbai,Sher E Punjab Colony,Rs. 22822 - 24648,Rs. 30336 - 33864,-
mumbai,Shimpoli,-,-,-
mumbai,Shreyas Colony,-,Rs. 25840 - 31280,-
mumbai,Shyam Nagar,-,Rs. 44506 - 50575,Rs. 46236 - 58064
mumbai,Siddharth Nagar,Rs. 16925 - 19152,Rs. 25288 - 28900,-
mumbai,Subhash Nagar,-,Rs. 31858 - 34247,-
mumbai,Sunder Nagar,Rs. 22772 - 24710,Rs. 30703 - 34447,-
mumbai,SV Patel Nagar,-,-,-
mumbai,Thakur Complex,Rs. 15788 - 17495,Rs. 25288 - 26732,Rs. 30196 - 37485
mumbai,Thakur Village,Rs. 17774 - 20374,Rs. 24692 - 28220,Rs. 31688 - 39610
mumbai,Umershetpada,Rs. 23375 - 25712,-,-
mumbai,Upper Govind Nagar,-,-,-
mumbai,Vaishali Nagar,-,-,-
mumbai,Veera Desai Road,Rs. 26414 - 29776,Rs. 38276 - 43744,-
mumbai,Versova,-,-,-
mumbai,Yari Road,Rs. 26775 - 31025,Rs. 47660 - 52198,-
mumbai,Yashodham,-,Rs. 30600 - 35955,-
mumbai,Yogi Nagar,-,-,-
mumbai,Bandra (East),-,Rs. 57800 - 67150,-
mumbai,Bandra (West),Rs. 44965 - 54251,Rs. 72004 - 87911,Rs. 131750 - 171275
mumbai,Bandra Kurla Complex,-,-,-
mumbai,Band Stand,Rs. 55080 - 59160,-,-
mumbai,Chuim,-,Rs. 71868 - 88825,-
mumbai,Gandhi Nagar,-,-,Rs. 148750 - 175525
mumbai,Hill Road,Rs. 47345 - 55867,-,-
mumbai,Juhu,Rs. 32120 - 37873,Rs. 60350 - 79900,Rs. 131782 - 158435
mumbai,Juhu Scheme,-,-,Rs. 129486 - 159253
mumbai,JVPD,-,-,Rs. 140828 - 163064
mumbai,Kala Nagar,-,-,Rs. 120870 - 152296
mumbai,Kalina,Rs. 28988 - 34986,Rs. 40185 - 49283,Rs. 65280 - 75480
mumbai,Khar,Rs. 38802 - 46750,Rs. 69700 - 85000,Rs. 103144 - 129241
mumbai,Khar West,Rs. 38802 - 46750,Rs. 69630 - 84915,Rs. 103426 - 129594
mumbai,Linking Road,-,-,-
mumbai,Mahim (West),Rs. 32725 - 35700,Rs. 52764 - 65752,-
mumbai,Mount Mary,-,Rs. 65450 - 87550,-
mumbai,Pali Hill,Rs. 48450 - 57630,Rs. 74800 - 90100,Rs. 158413 - 207917
mumbai,Pali Village,-,Rs. 71540 - 86156,-
mumbai,Santacruz (East),Rs. 27132 - 30524,Rs. 40185 - 47008,Rs. 60294 - 70689
mumbai,Santacruz (West),-,Rs. 58385 - 72981,Rs. 93266 - 116280
mumbai,Union Park,-,Rs. 72760 - 84584,-
mumbai,Vakola,Rs. 25245 - 28518,Rs. 38189 - 44064,Rs. 60690 - 67192
mumbai,Vidya Nagari,Rs. 36210 - 39270,Rs. 38984 - 46481,-
mumbai,Vile Parle (East),Rs. 31472 - 35287,Rs. 47685 - 52742,Rs. 71400 - 77520
mumbai,Vile Parle (West),Rs. 30903 - 37995,Rs. 54713 - 63072,-
mumbai,Yashwant Nagar,Rs. 25712 - 29452,-,-
mumbai,Ambedkar Nagar,Rs. 23990 - 26489,Rs. 36550 - 40800,Rs. 52190 - 60018
mumbai,Asha Nagar,-,-,-
mumbai,Bhandup (East),Rs. 17298 - 20570,Rs. 33150 - 36550,Rs. 54300 - 58477
mumbai,Bhandup (West),Rs. 20562 - 22568,Rs. 29304 - 33490,Rs. 40256 - 45288
mumbai,Chandivali,Rs. 24012 - 27854,Rs. 39100 - 42500,Rs. 56652 - 63240
mumbai,Dina Bama Estate,Rs. 22440 - 24480,Rs. 27044 - 28363,Rs. 40358 - 45403
mumbai,Friends Colony,Rs. 16371 - 18645,-,-
mumbai,Ganesh Nagar,Rs. 19168 - 21038,Rs. 29338 - 33099,Rs. 40162 - 47048
mumbai,Garodia Nagar,-,-,-
mumbai,Gavanpada,Rs. 14884 - 19699,-,-
mumbai,Ghatkopar (East),Rs. 20400 - 24480,Rs. 31365 - 38250,Rs. 53326 - 63248
mumbai,Ghatkopar West,Rs. 20385 - 22811,Rs. 37141 - 41268,Rs. 56419 - 65195
mumbai,Govind Nagar,Rs. 21063 - 24072,Rs. 27081 - 28586,-
mumbai,Hanuman Chowk,Rs. 17425 - 19550,-,-
mumbai,Hiranandani Gardens - Powai,Rs. 29325 - 34212,Rs. 52006 - 61384,Rs. 89972 - 109692
mumbai,HMPL Surya Nagar,-,Rs. 38208 - 40500,-
mumbai,Jagdusha Nagar,Rs. 16065 - 18742,-,-
mumbai,Jaydev Singh Nagar,Rs. 22652 - 24310,-,-
mumbai,Kanjur Marg (East),Rs. 19635 - 22440,Rs. 35734 - 39307,Rs. 54300 - 58477
mumbai,Kanjur Marg (west),Rs. 23371 - 26354,Rs. 36550 - 40800,Rs. 52190 - 60018
mumbai,Kannamwar Nagar I,-,-,-
mumbai,Kannamwar Nagar II,Rs. 12928 - 14918,-,-
mumbai,Kurla (East),Rs. 19516 - 21896,Rs. 27802 - 31559,-
mumbai,Kurla (west),Rs. 20318 - 23786,Rs. 37952 - 45220,Rs. 54770 - 61476
mumbai,LBS Marg,Rs. 21930 - 23970,Rs. 29038 - 31330,-
mumbai,Lok Milan Colony,Rs. 23162 - 28258,Rs. 44200 - 48450,Rs. 49836 - 54698
mumbai,Mhada Colony,-,-,Rs. 21573 - 27166
mumbai,Moti Nagar,-,-,-
mumbai,Mulund,Rs. 17298 - 19635,Rs. 28560 - 31824,Rs. 38658 - 43812
mumbai,Mulund (East),Rs. 16738 - 19993,Rs. 27102 - 29425,-
mumbai,Mulund (West),Rs. 17298 - 20102,Rs. 28858 - 32156,Rs. 39780 - 45084
mumbai,Mulund Colony,-,Rs. 26388 - 30158,-
mumbai,Nahur,Rs. 19542 - 20570,Rs. 29878 - 36338,-
mumbai,Nahur East,Rs. 15341 - 18217,-,-
mumbai,Nehru Nagar,Rs. 18896 - 21318,Rs. 25172 - 29614,-
mumbai,Nirmal Nagar,-,-,Rs. 40202 - 45227
mumbai,Panchkutir Ganesh Nagar,-,Rs. 63250 - 68116,-
mumbai,Pant Nagar,Rs. 19201 - 21552,-,Rs. 52224 - 58752
mumbai,Pestom Sagar Colony,Rs. 18870 - 24480,Rs. 31068 - 36125,-
mumbai,Powai,Rs. 26255 - 30631,Rs. 41862 - 50235,-
mumbai,Raheja Vihar,Rs. 26163 - 29070,Rs. 38212 - 42458,Rs. 53550 - 58650
mumbai,Rajiv Gandhi Nagar,Rs. 20884 - 23371,Rs. 26732 - 31790,-
mumbai,Sadan Wadi,-,-,-
mumbai,Sangharsh Nagar,-,Rs. 35700 - 41948,-
mumbai,Sarvodaya Nagar,Rs. 18700 - 20102,-,-
mumbai,Savarkar Nagar,Rs. 27310 - 33163,-,-
mumbai,Sion (East),-,-,-
mumbai,Tagore Nagar,-,-,-
mumbai,Tambe Nagar,-,Rs. 31686 - 33354,Rs. 36992 - 39168
mumbai,Tilak Nagar,Rs. 20332 - 22984,Rs. 32306 - 36246,-
mumbai,Tunga Village,Rs. 25967 - 29531,Rs. 38212 - 42458,-
mumbai,Valmiki Nagar,Rs. 22253 - 24276,-,-
mumbai,Veena Nagar,Rs. 17000 - 19125,-,-
mumbai,Vidya Vihar West,Rs. 19958 - 23451,-,-
mumbai,Vikhroli (East),Rs. 23343 - 27402,Rs. 48241 - 55388,Rs. 69360 - 78030
mumbai,Vikhroli (West),Rs. 20923 - 25572,Rs. 36307 - 40629,-
mumbai,Adaigaon,-,-,-
mumbai,Airoli,Rs. 13090 - 15428,Rs. 20655 - 24480,Rs. 30559 - 34925
mumbai,Belapur,Rs. 10032 - 12898,Rs. 21888 - 28016,Rs. 38097 - 49385
mumbai,Belpada,Rs. 9092 - 11964,Rs. 14994 - 18326,-
mumbai,Bonkode,Rs. 10200 - 12325,Rs. 19890 - 22185,-
mumbai,Devad,-,-,-
mumbai,Diva Gaothan,Rs. 9313 - 10582,-,-
mumbai,Dronagiri,-,-,-
mumbai,Gaothan,Rs. 8350 - 9668,-,-
mumbai,Ghansoli,Rs. 11302 - 13185,Rs. 22100 - 25500,Rs. 31280 - 37536
mumbai,Jeejamata Nagar,-,Rs. 24553 - 28330,Rs. 32531 - 35034
mumbai,Jijamata Nagar,-,Rs. 24378 - 27425,Rs. 34595 - 45602
mumbai,Jui Nagar,-,-,-
mumbai,Kalamboli,Rs. 7556 - 9176,Rs. 10271 - 11983,Rs. 11516 - 13435
mumbai,Kamothe,Rs. 7599 - 8612,Rs. 10973 - 12661,Rs. 13709 - 15994
mumbai,Karanjade,Rs. 4406 - 5386,-,-
mumbai,Karave Nagar,-,Rs. 30855 - 38335,Rs. 38786 - 47404
mumbai,Khalapur,Rs. 8160 - 10200,Rs. 15123 - 17959,Rs. 20536 - 24386
mumbai,Khanda Colony,-,Rs. 11475 - 13005,-
mumbai,Khandeshwar,Rs. 9256 - 9771,Rs. 12431 - 13260,-
mumbai,Kharghar,Rs. 7929 - 10407,Rs. 15943 - 18600,Rs. 20952 - 25882
mumbai,Kopara,-,Rs. 15606 - 17442,-
mumbai,Koperkhairane,Rs. 12622 - 14960,Rs. 20188 - 24225,-
mumbai,Kutak Bandhan,-,-,-
mumbai,Nerul,Rs. 11688 - 14025,Rs. 22100 - 28900,Rs. 40395 - 50819
mumbai,New Panvel,Rs. 7166 - 8599,Rs. 8854 - 11067,-
mumbai,New Sector-50 Nerul,Rs. 12750 - 16320,Rs. 21611 - 28527,-
mumbai,Old Panvel,-,Rs. 10940 - 12622,-
mumbai,Owe Village,-,-,-
mumbai,Palm Beach,Rs. 15343 - 18133,Rs. 28179 - 37866,Rs. 44625 - 54825
mumbai,Panvel,Rs. 7021 - 8526,Rs. 10873 - 12546,Rs. 13658 - 17072
mumbai,Petali,Rs. 4590 - 5100,-,-
mumbai,Phase-1 Petali,Rs. 4720 - 4720,-,-
mumbai,Rabale,-,Rs. 20311 - 22568,-
mumbai,Ranjanpada,-,-,-
mumbai,Rasayani,-,-,-
mumbai,Roadpali,Rs. 7735 - 8840,Rs. 10710 - 11602,-
mumbai,Sanpada,Rs. 15895 - 18700,Rs. 25032 - 30685,Rs. 39270 - 49980
mumbai,Seawoods,Rs. 12619 - 15046,Rs. 23317 - 31090,Rs. 39218 - 50037
mumbai,Sector-1 Airoli,Rs. 8840 - 11050,Rs. 15581 - 20324,-
mumbai,Sector-2 Kopar Khairane,Rs. 14790 - 18360,-,-
mumbai,Sector-2A Kopar Khairane,-,Rs. 20619 - 23792,-
mumbai,Sector-3 Airoli,-,Rs. 21174 - 24825,-
mumbai,Sector-3 Belpada,Rs. 9238 - 12155,Rs. 15827 - 19159,-
mumbai,Sector-3 Ulwe,Rs. 4628 - 5657,-,-
mumbai,Sector-4 Airoli,Rs. 13242 - 16185,-,-
mumbai,Sector-4 Nerul,-,Rs. 40509 - 46742,Rs. 66300 - 85000
mumbai,Sector-4A Koparkhairane,Rs. 11750 - 13219,-,-
mumbai,Sector-5 Kamothe,-,-,-
mumbai,Sector-5 Kharghar,-,Rs. 18546 - 21196,Rs. 20502 - 25058
mumbai,Sector-5 Kopar Khairane,Rs. 12155 - 15428,Rs. 18360 - 22185,-
mumbai,Sector-6 Airoli,Rs. 14960 - 17298,Rs. 21326 - 24608,-
mumbai,Sector-6 Ghansoli,Rs. 10696 - 13127,-,-
mumbai,Sector-6 Kharghar,Rs. 11164 - 12179,-,Rs. 27956 - 34034
mumbai,Sector-6 Kopar Khairane,Rs. 11411 - 13694,-,-
mumbai,Sector-6 Nerul,Rs. 7507 - 8915,-,Rs. 41616 - 45288
mumbai,Sector-6A Kamothe,-,-,-
mumbai,Sector-7 Ghansoli,-,Rs. 20332 - 21896,-
mumbai,Sector-7 Kamothe,-,-,-
mumbai,Sector-7 Kopar Khairane,-,Rs. 17790 - 21658,-
mumbai,Sector-8 Ghansoli,Rs. 16634 - 18650,Rs. 23664 - 25242,-
mumbai,Sector-8 Kharghar,Rs. 10809 - 11791,Rs. 17391 - 20869,Rs. 19815 - 24769
mumbai,Sector-8 Kopar Khairane,Rs. 13749 - 16498,Rs. 17947 - 23409,-
mumbai,Sector-8 Sanpada,-,-,-
mumbai,Sector-8 Ulwe,Rs. 4216 - 5270,Rs. 7249 - 9061,-
mumbai,Sector-8A Airoli,Rs. 14408 - 16328,Rs. 20999 - 24110,-
mumbai,Sector-9 Kamothe,-,-,-
mumbai,Sector-9 Sanpada,-,Rs. 21950 - 28322,-
mumbai,Sector-9 Ulwe,Rs. 5372 - 5909,-,Rs. 12856 - 14025
mumbai,Sector-10 New Panvel,Rs. 6630 - 7514,-,-
mumbai,Sector-10/B Ulwe,-,-,-
mumbai,Sector-10A Airoli,-,-,-
mumbai,Sector-11 Taloja,-,-,-
mumbai,Sector-12 Kamothe,-,-,-
mumbai,Sector-12 Kopar Khairane,Rs. 11539 - 13846,Rs. 19125 - 21420,-
mumbai,Sector-13 Kharghar,Rs. 8583 - 10014,Rs. 14226 - 16893,Rs. 21556 - 25598
mumbai,Sector-14 Koparkhairane,Rs. 13829 - 16213,Rs. 21420 - 23715,-
mumbai,Sector-14 Sanpada,Rs. 16958 - 19380,Rs. 23715 - 30600,Rs. 33278 - 39015
mumbai,Sector-14 Taloja,-,-,-
mumbai,Sector-15 Airoli,-,Rs. 13894 - 18946,-
mumbai,Sector-15 Ghansoli,Rs. 12689 - 14275,Rs. 20747 - 22476,-
mumbai,Sector-15 Sanpada,Rs. 15722 - 20143,Rs. 27251 - 30365,-
mumbai,Sector-16 Kharghar,Rs. 7752 - 8721,-,-
mumbai,Sector-16 Koparkhairane,-,Rs. 17707 - 21396,-
mumbai,Sector-16 Sanpada,Rs. 16524 - 19003,Rs. 24544 - 26031,-
mumbai,Sector-16 Taloja,-,-,-
mumbai,Sector-16 Ulwe,-,-,-
mumbai,Sector-17 Kamothe,Rs. 7357 - 8338,Rs. 11050 - 12750,-
mumbai,Sector-17 Kopar Khairane,-,Rs. 19727 - 21371,-
mumbai,Sector-18 Sanpada,-,Rs. 35530 - 39270,Rs. 51404 - 56419
mumbai,Sector-18 Ulwe,-,Rs. 7826 - 8696,-
mumbai,Sector-19 Airoli,Rs. 13558 - 15895,Rs. 24225 - 26648,-
mumbai,Sector-19 Koper Khairane,Rs. 8483 - 10180,Rs. 14025 - 15938,-
mumbai,Sector-19 Taloja,-,-,-
mumbai,Sector-19A Kopar Khairane,-,-,-
mumbai,Sector-20 Koparkhairane,Rs. 13260 - 16320,Rs. 22950 - 26350,-
mumbai,Sector-20 Nerul,Rs. 9443 - 12590,Rs. 16830 - 19890,-
mumbai,Sector-20 Roadpali,Rs. 6405 - 8152,Rs. 10248 - 13042,-
mumbai,Sector-20 Taloja,-,-,-
mumbai,Sector-20B Airoli,Rs. 14025 - 16830,Rs. 22950 - 26010,-
mumbai,Sector-22 Kopar Khairane,Rs. 11688 - 13558,-,-
mumbai,Sector-23 Juinagar,-,-,-
mumbai,Sector-23 Kharghar,-,-,-
mumbai,Sector-23 Taloja,-,-,-
mumbai,Sector-24 Kamothe,-,-,-
mumbai,Sector-25 Kamothe,Rs. 7739 - 9287,-,-
mumbai,Sector-25 Khandeshhwar,Rs. 9706 - 10217,Rs. 13260 - 13260,-
mumbai,Sector-27 Kharghar,Rs. 6785 - 7307,Rs. 16356 - 19082,Rs. 20461 - 21665
mumbai,Sector-27 Nerul,-,Rs. 17404 - 20719,-
mumbai,Sector-28 Nerul,-,-,Rs. 53405 - 58882
mumbai,Sector-29C Airoli,Rs. 12990 - 15395,Rs. 22491 - 25823,-
mumbai,Sector-30 Belapur,-,Rs. 25372 - 28417,-
mumbai,Sector-30 Ghansoli,Rs. 12973 - 17962,Rs. 24786 - 25612,-
mumbai,Sector-34 Kharghar,Rs. 7902 - 8395,-,-
mumbai,Sector-34A Kharghar,-,Rs. 20757 - 23588,Rs. 28792 - 30163
mumbai,Sector-34B Kharghar,-,Rs. 13222 - 16333,-
mumbai,Sector-35 Kamothe,Rs. 8010 - 8511,Rs. 10387 - 11985,-
mumbai,Sector-35D Kharghar,Rs. 8418 - 9471,Rs. 14960 - 18700,Rs. 19720 - 24650
mumbai,Sector-35E Kharghar,Rs. 8242 - 10817,Rs. 15150 - 17991,Rs. 20536 - 24386
mumbai,Sector-35G Kharghar,Rs. 10924 - 11965,Rs. 14277 - 16796,Rs. 18958 - 22513
mumbai,Sector-37 Taloja,-,-,-
mumbai,Sector-42A Seawoods,-,-,-
mumbai,Sector-44A Seawoods,Rs. 11772 - 13656,-,-
mumbai,Sector-46 Seawoods,Rs. 10117 - 11036,Rs. 32640 - 36720,Rs. 35391 - 46766
mumbai,Sector-48 Seawoods,Rs. 10067 - 11506,-,-
mumbai,Sector-50 Seawoods,Rs. 12495 - 15494,-,Rs. 34731 - 43993
mumbai,Sector-58 Seawoods,-,Rs. 36465 - 43010,Rs. 51232 - 56771
mumbai,Sector-58A Seawoods,-,-,Rs. 46803 - 56656
mumbai,Sector 1 Kopar Khairane,Rs. 11492 - 13260,-,-
mumbai,Sector 1 Sanpada,Rs. 15317 - 18470,Rs. 20658 - 22872,-
mumbai,Sector 2 Kharghar,-,Rs. 17000 - 20400,Rs. 22610 - 26180
mumbai,Sector 2 Ulwe,Rs. 4938 - 5926,Rs. 7788 - 8653,-
mumbai,Sector 3 Kharghar,Rs. 10710 - 11730,Rs. 14450 - 17000,-
mumbai,Sector 4 Kharghar,Rs. 11602 - 12995,Rs. 15342 - 18572,Rs. 24047 - 27844
mumbai,Sector 5 Ghansoli,Rs. 11688 - 14025,-,-
mumbai,Sector 5 Ulwe,-,-,-
mumbai,Sector 6 Kamothe,-,-,-
mumbai,Sector 7 Airoli,Rs. 15776 - 17748,Rs. 22610 - 25840,Rs. 30409 - 33788
mumbai,Sector 7 Kharghar,-,Rs. 21134 - 23890,Rs. 24140 - 28968
mumbai,Sector 8 Airoli,Rs. 14280 - 17612,Rs. 19426 - 24656,-
mumbai,Sector 9 Airoli,Rs. 10625 - 12750,Rs. 16618 - 20230,-
mumbai,Sector 9 Nerul,-,-,-
mumbai,Sector 10 Kamothe,-,-,-
mumbai,Sector 10 Kharghar,Rs. 9642 - 10656,Rs. 16157 - 18850,Rs. 21458 - 27770
mumbai,Sector 11 Belapur,Rs. 13196 - 13685,-,-
mumbai,Sector 11 Kamothe,-,-,-
mumbai,Sector 11 Kharghar,Rs. 9200 - 10455,Rs. 14535 - 18360,-
mumbai,Sector 11 Koparkhairane,Rs. 13540 - 15797,Rs. 20995 - 25840,Rs. 28688 - 37868
mumbai,Sector 12 Kharghar,Rs. 9877 - 12346,Rs. 17000 - 18700,Rs. 22185 - 27115
mumbai,Sector 12 Vashi,Rs. 14790 - 17850,Rs. 23324 - 30821,Rs. 38569 - 42075
mumbai,Sector 13 Sanpada,Rs. 13260 - 15470,-,-
mumbai,Sector 14 Kamothe,-,-,-
mumbai,Sector 14 Kharghar,-,Rs. 16333 - 17888,-
mumbai,Sector 14 Vashi,-,-,Rs. 30464 - 40256
mumbai,Sector 15 Belapur,-,Rs. 24650 - 28900,Rs. 44217 - 54534
mumbai,Sector 15 Kharghar,-,Rs. 19414 - 21355,Rs. 22063 - 25740
mumbai,Sector 15 Kopar Khairane,Rs. 11648 - 15046,Rs. 19380 - 21802,-
mumbai,Sector 16 Ghansoli,Rs. 12177 - 13114,Rs. 16810 - 18210,-
mumbai,Sector 16 Kamothe,-,Rs. 11080 - 11818,-
mumbai,Sector 16 Vashi,-,Rs. 23715 - 26775,-
mumbai,Sector 16A Nerul,-,-,Rs. 53465 - 54910
mumbai,Sector 17 Ulwe,Rs. 4529 - 5535,Rs. 6548 - 8186,-
mumbai,Sector 17 Vashi,Rs. 17340 - 20910,Rs. 28727 - 32951,-
mumbai,Sector 18 Kamothe,Rs. 7561 - 8065,Rs. 10752 - 11579,-
mumbai,Sector 18 Kharghar,Rs. 9432 - 12410,Rs. 14520 - 16133,Rs. 16774 - 20645
mumbai,Sector 19 Kamothe,Rs. 7446 - 8935,Rs. 11050 - 11900,-
mumbai,Sector 19 Kharghar,Rs. 9690 - 10710,Rs. 15592 - 18343,Rs. 21634 - 26442
mumbai,Sector 19 Nerul,Rs. 14408 - 15848,Rs. 19380 - 22610,Rs. 21187 - 24076
mumbai,Sector 19 Ulwe,-,Rs. 7574 - 9256,-
mumbai,Sector 19A Nerul,Rs. 14816 - 16297,Rs. 21917 - 26788,-
mumbai,Sector 20 Airoli,Rs. 12622 - 14492,Rs. 18360 - 23715,-
mumbai,Sector 20 Belapur,Rs. 10370 - 12444,-,-
mumbai,Sector 20 Kamothe,Rs. 7650 - 8160,Rs. 10037 - 10873,-
mumbai,Sector 20 Kharghar,Rs. 9945 - 10940,Rs. 15300 - 19550,Rs. 22139 - 24599
mumbai,Sector 20 Ulwe,Rs. 5296 - 6355,Rs. 9640 - 11393,-
mumbai,Sector 21 Ghansoli,Rs. 10285 - 11688,Rs. 15440 - 19116,-
mumbai,Sector 21 Kamothe,Rs. 7116 - 8641,Rs. 11050 - 11900,Rs. 14851 - 15994
mumbai,Sector 21 Kharghar,Rs. 10481 - 12136,Rs. 15927 - 18582,-
mumbai,Sector 21 Nerul,Rs. 14025 - 15895,Rs. 20597 - 22974,-
mumbai,Sector 21 Ulwe,Rs. 5338 - 5872,Rs. 7941 - 10588,Rs. 12452 - 14943
mumbai,Sector 22 Kamothe,Rs. 7318 - 7841,Rs. 11050 - 11900,Rs. 14749 - 15978
mumbai,Sector 23 Ghansoli,Rs. 10713 - 11645,-,-
mumbai,Sector 23 Nerul,Rs. 12622 - 13558,Rs. 16958 - 20995,-
mumbai,Sector 23 Ulwe,-,-,-
mumbai,Sector 25 Nerul,-,Rs. 23541 - 25976,-
mumbai,Sector 26 Vashi,Rs. 13614 - 16045,Rs. 21128 - 25191,-
mumbai,Sector 28 Vashi,Rs. 15708 - 18326,Rs. 19550 - 23800,Rs. 29804 - 34772
mumbai,Sector 29 Vashi,-,Rs. 23837 - 27946,-
mumbai,Sector 30 Kharghar,-,-,-
mumbai,Sector 34 Kamothe,Rs. 7535 - 8540,Rs. 12928 - 16376,-
mumbai,Sector 34C Kharghar,-,Rs. 13090 - 15895,-
mumbai,Sector 35I Kharghar,Rs. 9486 - 10540,Rs. 12750 - 15300,Rs. 16934 - 20562
mumbai,Sector 36 Kamothe,Rs. 7535 - 8540,Rs. 10608 - 12240,-
mumbai,Sector 36 Kharghar,Rs. 6450 - 6910,Rs. 13426 - 15216,Rs. 17802 - 21617
mumbai,Sector 36 Seawoods,-,-,-
mumbai,Sector 40 Seawoods,Rs. 13449 - 14943,Rs. 20804 - 24132,-
mumbai,Sector 42 Seawoods,Rs. 14586 - 15558,Rs. 22100 - 25500,-
mumbai,Sector 44 Seawoods,Rs. 12266 - 15096,Rs. 18221 - 21389,Rs. 34904 - 40922
mumbai,Shilphata,Rs. 7069 - 8583,Rs. 10543 - 12050,-
mumbai,Takka Colony,-,-,-
mumbai,Taloja,Rs. 4582 - 5092,Rs. 7130 - 7922,Rs. 16575 - 17850
mumbai,Taloja Panchanand,Rs. 5194 - 6232,Rs. 7650 - 9350,-
mumbai,Ulwe,Rs. 5100 - 5610,Rs. 7619 - 9313,Rs. 11586 - 13903
mumbai,Vashi,Rs. 15045 - 19057,Rs. 22800 - 27686,Rs. 33320 - 41650
mumbai,Vichumbe,Rs. 5844 - 5844,Rs. 7268 - 8075,-
mumbai,Abhyudaya Nagar,-,Rs. 63954 - 68395,-
mumbai,Adarsh Nagar,Rs. 18034 - 23603,-,-
mumbai,Agripada,-,-,Rs. 320790 - 364140
mumbai,Altamount Road,Rs. 71400 - 90525,-,-
mumbai,Apollo Bandar,Rs. 54060 - 58650,-,-
mumbai,Breach Candy,Rs. 73480 - 90643,Rs. 119340 - 138720,Rs. 202618 - 232269
mumbai,Century Bazaar,-,Rs. 62345 - 80416,-
mumbai,Chamundeshwari Nagar,-,Rs. 131835 - 142120,Rs. 185426 - 201824
mumbai,Chandrakant Dhuru Wadi,-,-,Rs. 158253 - 171896
mumbai,Churchgate,-,-,Rs. 159173 - 208823
mumbai,Colaba,Rs. 50490 - 56100,Rs. 79700 - 94881,Rs. 160380 - 190281
mumbai,Cuffe Parade,-,Rs. 110106 - 125589,Rs. 167290 - 200483
mumbai,Cusrow Baug Colony,Rs. 51000 - 57630,-,-
mumbai,Dadar,Rs. 27399 - 32416,Rs. 65450 - 79050,Rs. 132567 - 172479
mumbai,Dadar (East),Rs. 35182 - 37592,Rs. 59500 - 72250,Rs. 122464 - 139753
mumbai,Dadar (West),Rs. 27158 - 32130,Rs. 65450 - 80750,Rs. 134152 - 175539
mumbai,Elphinestone Road,Rs. 28948 - 32164,-,-
mumbai,Gamdevi,-,-,-
mumbai,Gandhi Nagar Worli,-,Rs. 64061 - 72170,-
mumbai,Girgaon,-,-,-
mumbai,Hanuman Nagar,-,-,Rs. 173442 - 218492
mumbai,Hindu Colony,-,-,-
mumbai,Jacob Circle,-,Rs. 123831 - 139182,Rs. 186405 - 210970
mumbai,Kemps Corner,-,Rs. 123250 - 139400,-
mumbai,Koliwada,-,-,Rs. 149989 - 196974
mumbai,Lower Parel,Rs. 29325 - 34425,Rs. 71536 - 89420,Rs. 189090 - 232559
mumbai,Lower Parel East,-,Rs. 63240 - 77520,-
mumbai,Lower Parel West,Rs. 21258 - 26486,Rs. 71400 - 79900,Rs. 155252 - 172663
mumbai,Mahalaxmi,Rs. 35764 - 42916,Rs. 117443 - 128775,Rs. 172380 - 195585
mumbai,Malabar Hill,Rs. 62730 - 69870,Rs. 122400 - 153000,Rs. 202130 - 250920
mumbai,Marine Drive,-,-,-
mumbai,Matunga,Rs. 34884 - 39015,Rs. 49946 - 63777,-
mumbai,Matunga East,Rs. 36465 - 41140,Rs. 68000 - 82450,-
mumbai,Matunga West,Rs. 34425 - 39015,Rs. 48344 - 58756,-
mumbai,Mumbai Central,-,-,-
mumbai,Napean Sea Road,-,-,Rs. 188700 - 238000
mumbai,Parel,Rs. 28532 - 34494,Rs. 62832 - 72352,Rs. 87210 - 107559
mumbai,Parmanand Wadi,-,Rs. 62944 - 69620,Rs. 88358 - 96390
mumbai,Peddar Road,-,Rs. 93745 - 106189,-
mumbai,Prabhadevi,Rs. 26334 - 31295,Rs. 68493 - 86700,Rs. 135830 - 176290
mumbai,Shivaji Park,Rs. 38743 - 41896,Rs. 62475 - 69139,-
mumbai,Tardeo,-,-,-
mumbai,Upper Worli,Rs. 38255 - 44140,-,-
mumbai,Walkeshwar,-,-,Rs. 187680 - 208080
mumbai,Worli,Rs. 26392 - 34808,Rs. 74078 - 89250,Rs. 154460 - 195769
mumbai,Worli Hill,Rs. 51382 - 59670,Rs. 79050 - 87550,-
mumbai,Worli Naka,Rs. 34918 - 41990,Rs. 68133 - 72558,-
mumbai,Worli Seaface,-,Rs. 70543 - 84109,Rs. 116025 - 142800
mumbai,Bhakti Park,-,Rs. 47603 - 53096,Rs. 70991 - 78543
mumbai,Byculla,Rs. 24072 - 26520,-,-
mumbai,Byculla East,-,-,-
mumbai,Byculla West,Rs. 25075 - 27200,-,-
mumbai,Chembur,Rs. 23371 - 27349,Rs. 37523 - 44194,Rs. 54305 - 62944
mumbai,Chembur (East),Rs. 25075 - 28586,Rs. 38250 - 45050,Rs. 54342 - 62988
mumbai,Chembur (West),Rs. 20026 - 22529,Rs. 27455 - 32512,-
mumbai,Collectors Colony Chembur,Rs. 24840 - 26751,Rs. 31633 - 35850,-
mumbai,Deonar,-,Rs. 40429 - 47311,Rs. 60792 - 73457
mumbai,Govandi,-,-,-
mumbai,Govandi East,Rs. 24778 - 28985,-,-
mumbai,Lalbaug,-,Rs. 63580 - 67320,Rs. 107273 - 111452
mumbai,Mankhurd,-,-,-
mumbai,Mazgaon,Rs. 31714 - 36244,Rs. 52360 - 61710,-
mumbai,Nagesh Patilwadi,-,Rs. 36210 - 38926,-
mumbai,Postal Colony,-,Rs. 38174 - 42415,Rs. 41140 - 47685
mumbai,RCF Colony Chembur,-,Rs. 30880 - 38968,-
mumbai,Sewri,Rs. 24055 - 26942,-,Rs. 72383 - 85348
mumbai,Sindhi Society Chembur,Rs. 26444 - 29438,Rs. 34722 - 41182,Rs. 50490 - 55080
mumbai,Swastik Park,Rs. 20522 - 22660,Rs. 35666 - 41908,Rs. 49082 - 51128
mumbai,Tilak Nagar,Rs. 21613 - 23912,Rs. 31688 - 37233,Rs. 40800 - 42840
mumbai,Tolaram Colony,-,Rs. 29410 - 38968,-
mumbai,Union Park,-,Rs. 36152 - 42792,-
mumbai,Wadala,Rs. 31640 - 34517,Rs. 47369 - 55264,Rs. 59900 - 67886
mumbai,Wadala East,Rs. 29060 - 31261,Rs. 44870 - 49949,Rs. 61883 - 69782
mumbai,Wadala West,Rs. 39046 - 42299,Rs. 48746 - 55967,-
bangalore,Basaveshwara Nagar,-,Rs. 18360 - 22440,Rs. 27294 - 30166
bangalore,BEML Layout,-,-,-
bangalore,Binny Pete,-,-,Rs. 33596 - 44347
bangalore,Dasanapura,-,Rs. 8995 - 11070,-
bangalore,Jalahalli West,-,Rs. 13120 - 15744,-
bangalore,Kenchenhalli,-,Rs. 11934 - 13923,-
bangalore,Kengeri,Rs. 4972 - 5355,Rs. 9060 - 11531,Rs. 13184 - 16779
bangalore,Kengeri Satellite Town,-,Rs. 9292 - 10841,-
bangalore,Mahalakshmi Layout,-,-,Rs. 28471 - 33894
bangalore,Mallasandra,-,Rs. 14662 - 17595,-
bangalore,Mathikere,-,Rs. 13005 - 15172,-
bangalore,Mysore Road,Rs. 5304 - 5712,Rs. 10111 - 10888,Rs. 12668 - 15836
bangalore,Nagarbhavi,-,-,-
bangalore,Nelamangala,-,Rs. 8303 - 11070,-
bangalore,Rajaji Nagar,-,Rs. 35731 - 42646,-
bangalore,Raja Rajeshwari Nagar,-,Rs. 11424 - 14280,Rs. 13071 - 16636
bangalore,Raja Rajeshwari Nagar 5th Stage,-,-,-
bangalore,Tumkur Road,-,-,Rs. 16881 - 21383
bangalore,Vijayanagar,-,Rs. 12750 - 15300,-
bangalore,1A Block Koramangala,-,Rs. 28322 - 29334,-
bangalore,1st Block Koramangala,-,-,-
bangalore,1st Phase JP Nagar,Rs. 10417 - 12610,Rs. 18360 - 19380,-
bangalore,2nd Stage Arekere Mico Layout,-,Rs. 17170 - 19746,-
bangalore,3rd Block Koramangala,-,-,Rs. 45262 - 51298
bangalore,4th Block Koramangala,-,Rs. 23949 - 28114,-
bangalore,5th Phase JP Nagar,-,Rs. 14662 - 17595,Rs. 19625 - 22078
bangalore,6th Phase JP Nagar,-,-,Rs. 26698 - 34115
bangalore,7th Phase JP Nagar,-,-,Rs. 26027 - 28630
bangalore,8th Phase JP Nagar,-,Rs. 12067 - 15779,-
bangalore,9th Phase JP Nagar,-,-,-
bangalore,Adugodi,-,-,Rs. 55339 - 61064
bangalore,Akshaya Nagar,-,Rs. 14280 - 16320,Rs. 19016 - 21733
bangalore,Akshaya Vana,-,Rs. 11602 - 13260,Rs. 15415 - 18972
bangalore,Amblipura,-,-,-
bangalore,Ananth Nagar,-,Rs. 9690 - 12112,-
bangalore,Anekal,-,Rs. 8160 - 10200,-
bangalore,Anjanapura,-,Rs. 8424 - 10108,-
bangalore,Arekere,Rs. 9615 - 10645,Rs. 15895 - 19635,-
bangalore,Attibele,-,Rs. 5804 - 6771,-
bangalore,Balaji Gardens Layout,-,Rs. 11411 - 12933,-
bangalore,Banashankari,-,Rs. 13260 - 16320,Rs. 19040 - 24480
bangalore,Banashankari Stage III,-,Rs. 12155 - 14960,Rs. 24072 - 30090
bangalore,Bannerghatta Road,-,Rs. 14025 - 17765,Rs. 19431 - 23317
bangalore,Basapura,-,Rs. 13257 - 16097,Rs. 14127 - 18836
bangalore,Basavangudi,-,Rs. 19635 - 23375,Rs. 32987 - 37110
bangalore,Begur,-,-,Rs. 13592 - 15682
bangalore,Begur Road,-,Rs. 12750 - 15300,Rs. 13882 - 17353
bangalore,Bellandur,-,Rs. 21243 - 24140,Rs. 29988 - 35700
bangalore,Bikasipura,-,Rs. 11127 - 12839,Rs. 19074 - 20808
bangalore,Billekahalli,-,-,Rs. 26408 - 33743
bangalore,Bohra Layout,-,Rs. 10686 - 12976,-
bangalore,Bommanahalli,-,Rs. 12724 - 15269,Rs. 17850 - 21420
bangalore,Bommasandra,-,Rs. 9200 - 10873,-
bangalore,BTM 2nd Stage,Rs. 9649 - 11404,Rs. 16683 - 19317,Rs. 31273 - 37230
bangalore,BTM Layout,Rs. 9350 - 11050,Rs. 17000 - 19550,Rs. 31594 - 36108
bangalore,Carmelaram,-,Rs. 20358 - 21986,Rs. 22491 - 24740
bangalore,Chandapura,Rs. 5879 - 6718,Rs. 8058 - 9401,Rs. 9469 - 11363
bangalore,Chikkalasandra,-,Rs. 11459 - 11459,-
bangalore,Chikku Lakshmaiah Layout,-,-,Rs. 55339 - 61064
bangalore,Choodasandra,-,-,Rs. 13811 - 18414
bangalore,Devarabisanahalli,-,-,Rs. 35006 - 37699
bangalore,Devarachikkanahalli,-,Rs. 11745 - 13423,Rs. 16011 - 17243
bangalore,Doddakallasandra,-,-,Rs. 14450 - 17340
bangalore,Doddathoguru,Rs. 7255 - 8222,Rs. 11864 - 15254,Rs. 17672 - 20196
bangalore,Dollars Layout,-,-,Rs. 32130 - 33660
bangalore,Ejipura,-,-,-
bangalore,Electronic City,-,Rs. 11900 - 15300,Rs. 14586 - 19074
bangalore,Electronic City Phase II,-,Rs. 10498 - 12920,Rs. 15625 - 18973
bangalore,Electronics City Phase 1,-,Rs. 14022 - 16651,Rs. 17620 - 21145
bangalore,Gollahalli,-,Rs. 12852 - 14688,Rs. 14678 - 18347
bangalore,Gottigere,-,Rs. 9378 - 12788,Rs. 14025 - 17850
bangalore,Green Glen Layout,-,Rs. 21384 - 23421,Rs. 27455 - 31790
bangalore,Gubbalala,-,Rs. 15300 - 17340,Rs. 18785 - 21675
bangalore,Harlur,-,Rs. 19635 - 26180,Rs. 25291 - 29284
bangalore,Hongasandra,-,Rs. 12444 - 13274,-
bangalore,Hosa Road,-,Rs. 13107 - 13981,Rs. 13901 - 18178
bangalore,Hosur Road,-,Rs. 13043 - 16521,Rs. 17850 - 22610
bangalore,HSR Layout,Rs. 11975 - 15467,Rs. 17765 - 21505,Rs. 26502 - 30687
bangalore,Hulimavu,-,Rs. 13974 - 16769,Rs. 20272 - 24327
bangalore,Iblur Village,-,-,-
bangalore,Ittamadu,-,Rs. 11220 - 13090,-
bangalore,Jayanagar,-,Rs. 20570 - 22440,Rs. 33235 - 37570
bangalore,Jigani,-,Rs. 8480 - 10022,Rs. 10430 - 11472
bangalore,JP Nagar,-,Rs. 15042 - 19742,Rs. 24266 - 29658
bangalore,Kaggalipura,-,-,Rs. 9988 - 12984
bangalore,Kaikondrahalli,-,-,-
bangalore,Kalena Agrahara,-,Rs. 17701 - 20825,Rs. 21760 - 24480
bangalore,Kammasandra,-,Rs. 10044 - 12362,-
bangalore,Kanakapura,-,-,Rs. 10412 - 12495
bangalore,Kanakpura Road,-,Rs. 12708 - 15640,Rs. 16228 - 20285
bangalore,Karuna Nagar,-,Rs. 16592 - 19703,Rs. 19927 - 23443
bangalore,Kodichikkanahalli,-,Rs. 12852 - 14458,Rs. 16660 - 20230
bangalore,Konanakunte,-,Rs. 10248 - 13042,Rs. 13600 - 17680
bangalore,Koramangala,Rs. 14918 - 19338,Rs. 24969 - 30961,Rs. 39015 - 50575
bangalore,Kothannur,-,Rs. 11503 - 14158,-
bangalore,Kudlu,-,Rs. 14008 - 17510,Rs. 17041 - 19475
bangalore,Kumaraswami Layout,-,-,-
bangalore,Lakshmi Layout,-,Rs. 16312 - 19746,Rs. 23106 - 27439
bangalore,Lingadheeranahalli,-,-,Rs. 17303 - 19774
bangalore,Mallasandra,-,-,-
bangalore,Maragondanahalli,-,-,Rs. 16817 - 20181
bangalore,Munivenkatppa Layout,-,-,Rs. 31747 - 42951
bangalore,Neeladri Nagar,Rs. 8670 - 11220,Rs. 12750 - 14450,Rs. 18488 - 20952
bangalore,Padmanabhanagar,-,Rs. 13107 - 14855,-
bangalore,Panduranga Nagar,-,Rs. 17518 - 22385,Rs. 25921 - 31378
bangalore,Rajapura,-,Rs. 9532 - 10894,Rs. 10843 - 12650
bangalore,Rayasandra,Rs. 5773 - 7216,Rs. 11370 - 13994,Rs. 13901 - 17109
bangalore,Roopena Agrahara,-,Rs. 13600 - 16150,-
bangalore,Sahyadri Layout,-,Rs. 21284 - 25541,Rs. 27285 - 31378
bangalore,Sarjapura - Attibele Road,-,Rs. 6040 - 7687,Rs. 10883 - 12862
bangalore,Sector 1 HSR Layout,-,Rs. 20551 - 22420,Rs. 29750 - 32725
bangalore,Sector 2 HSR Layout,Rs. 13260 - 16830,Rs. 18459 - 22346,Rs. 25245 - 32258
bangalore,Sector 7 HSR Layout,-,Rs. 23746 - 26714,-
bangalore,Shan Boga Colony,-,-,-
bangalore,Shikaripalya,-,-,Rs. 17255 - 19720
bangalore,Silk Board,Rs. 8772 - 11404,Rs. 15172 - 18742,Rs. 21675 - 28050
bangalore,Singasandra,-,Rs. 12495 - 15172,-
bangalore,Somasundara Palya,-,Rs. 16256 - 19125,-
bangalore,Subramanyapura,-,Rs. 12240 - 16320,Rs. 17340 - 20230
bangalore,Talaghattapura,-,-,Rs. 12750 - 16575
bangalore,Uttarahalli,-,Rs. 9818 - 11602,Rs. 13770 - 16065
bangalore,Vasantha Vallabha Nagar,-,-,Rs. 17629 - 21155
bangalore,Vijaya Bank Layout,-,Rs. 13257 - 16097,Rs. 18028 - 20432
bangalore,Vishwapriya Layout,-,-,-
bangalore,Vittasandra,-,Rs. 17600 - 18635,-
bangalore,Yelenahalli,-,-,-
bangalore,Ashok Nagar,-,Rs. 45186 - 54223,-
bangalore,Benson Town,-,-,Rs. 46410 - 55335
bangalore,Cox Town,-,Rs. 21420 - 24098,-
bangalore,Cunningham Road,-,-,-
bangalore,Frazer Town,-,Rs. 20570 - 23375,-
bangalore,Lavelle Road,-,-,Rs. 76644 - 103572
bangalore,M.G Road,-,Rs. 32538 - 38454,Rs. 43435 - 52742
bangalore,Richards Town,-,-,Rs. 38802 - 49385
bangalore,Richmond Road,-,Rs. 30916 - 35333,Rs. 59949 - 76486
bangalore,Richmond Town,-,Rs. 30916 - 35333,Rs. 57810 - 76392
bangalore,Shanthala Nagar,-,-,Rs. 76644 - 103572
bangalore,Ulsoor,Rs. 12186 - 15232,Rs. 20528 - 24990,Rs. 33724 - 42521
bangalore,Vittal Mallya Road,-,Rs. 43520 - 48960,-
bangalore,3rd Block HBR Layout,-,Rs. 18700 - 22440,-
bangalore,AECS Layout,Rs. 13056 - 14144,Rs. 19550 - 23460,Rs. 23611 - 31068
bangalore,Ambalipura,-,Rs. 19635 - 25245,Rs. 29920 - 34000
bangalore,Ambedkar Nagar,-,-,Rs. 25840 - 28560
bangalore,Anjappa Layout,Rs. 10947 - 11353,-,-
bangalore,Ardendale,-,-,Rs. 17340 - 20230
bangalore,Badavala Nagar,Rs. 10542 - 11758,Rs. 16949 - 18644,-
bangalore,Balagere,Rs. 14849 - 17598,Rs. 18700 - 21250,-
bangalore,Banaswadi,Rs. 7973 - 10251,Rs. 16830 - 17765,Rs. 19984 - 23511
bangalore,Belatur,-,Rs. 14458 - 16386,-
bangalore,Belatur Colony,-,-,-
bangalore,Bhoganhalli,-,Rs. 19635 - 25245,Rs. 29113 - 33272
bangalore,B Narayanapura,Rs. 11492 - 12376,Rs. 16958 - 19635,-
bangalore,Brookefield,-,Rs. 19207 - 23780,Rs. 23837 - 30459
bangalore,Cambridge Layout,-,Rs. 25245 - 28050,Rs. 40928 - 50477
bangalore,Channasandra,-,Rs. 12686 - 14378,Rs. 14498 - 16728
bangalore,Chelekare,-,Rs. 16578 - 18651,-
bangalore,Chinnapanahalli,-,Rs. 19380 - 22440,-
bangalore,CMH Road,-,Rs. 24480 - 27540,-
bangalore,Cooke Town,Rs. 13834 - 16600,Rs. 20570 - 23375,-
bangalore,CV Raman Nagar,Rs. 10924 - 12485,Rs. 17243 - 20117,Rs. 24082 - 32110
bangalore,Defence Colony,-,-,-
bangalore,Devarabeesana Halli,-,-,-
bangalore,Doddabanahalli,-,Rs. 8466 - 9877,-
bangalore,Doddakannelli,-,Rs. 18836 - 22603,Rs. 22865 - 26295
bangalore,Dodda Nekkundi,-,Rs. 19429 - 22079,Rs. 24044 - 26334
bangalore,Dodda Nekkundi Extension,-,-,-
bangalore,Doddanekundi,Rs. 9955 - 12444,Rs. 17595 - 21505,-
bangalore,Domlur,Rs. 12622 - 14492,Rs. 27540 - 31620,-
bangalore,Dooravani Nagar,-,-,Rs. 27174 - 29538
bangalore,EPIP Zone,-,Rs. 23297 - 26209,Rs. 35998 - 44179
bangalore,Garudachar Palya,-,-,Rs. 26442 - 30048
bangalore,GM Palaya,Rs. 11624 - 12554,Rs. 15794 - 17652,Rs. 21675 - 24225
bangalore,Gunjur,-,-,-
bangalore,Hagadur,-,Rs. 12340 - 14985,-
bangalore,HAL 2nd Stage,Rs. 11730 - 14174,Rs. 22440 - 27115,Rs. 27668 - 34255
bangalore,HAL 3rd Stage,-,Rs. 21212 - 23056,-
bangalore,Harlur Road,-,Rs. 23991 - 25911,Rs. 27455 - 31790
bangalore,HBR Layout,Rs. 7948 - 10752,Rs. 16242 - 19108,Rs. 21932 - 26549
bangalore,Hoodi,-,Rs. 17846 - 20664,Rs. 22658 - 26656
bangalore,Hoskote,-,Rs. 7517 - 8884,Rs. 10276 - 13078
bangalore,HRBR Layout,-,Rs. 18742 - 21420,Rs. 32130 - 35190
bangalore,Indira Nagar,Rs. 13260 - 15810,Rs. 22482 - 27370,Rs. 57375 - 61625
bangalore,Indira Nagar Stage 2,-,Rs. 21505 - 27115,Rs. 66555 - 71485
bangalore,ITPL,-,Rs. 17085 - 20502,Rs. 19135 - 23919
bangalore,Jeevan Bima Nagar,-,Rs. 19149 - 20890,-
bangalore,Kadubeesanahalli,-,Rs. 19903 - 23694,Rs. 28560 - 34000
bangalore,Kadugodi,-,Rs. 13528 - 16233,Rs. 18551 - 22262
bangalore,Kaggadasapura,Rs. 9764 - 11624,Rs. 15172 - 17850,Rs. 18105 - 21726
bangalore,Kalyan Nagar,Rs. 8882 - 10285,Rs. 15286 - 19108,Rs. 21420 - 26180
bangalore,Kammanahalli,-,Rs. 14450 - 17850,Rs. 22950 - 26775
bangalore,Kannamangala,-,Rs. 12638 - 14443,Rs. 16320 - 20400
bangalore,Kartik Nagar,Rs. 9350 - 12325,Rs. 17595 - 20528,Rs. 22950 - 29325
bangalore,Kasavanhalli,-,Rs. 17167 - 20028,Rs. 23730 - 27685
bangalore,Kasturi Nagar,Rs. 10282 - 11424,-,Rs. 21299 - 26311
bangalore,Kaverappa Layout,-,-,-
bangalore,Kodigehalli,-,Rs. 12126 - 13858,-
bangalore,Kodihalli,-,Rs. 18700 - 22440,-
bangalore,KR Puram,-,Rs. 11890 - 14634,-
bangalore,Kundalahalli,-,Rs. 16150 - 22100,Rs. 22340 - 28910
bangalore,Kundalahalli Colony,-,Rs. 21866 - 24990,-
bangalore,Lakshminarayana Pura,-,Rs. 24643 - 29777,Rs. 24854 - 32310
bangalore,Lingarajapuram,-,-,-
bangalore,Mahadevpura,Rs. 11492 - 12376,Rs. 17054 - 19747,Rs. 24650 - 29580
bangalore,Malleshpalya,Rs. 10341 - 12221,Rs. 15042 - 16812,-
bangalore,Marathahalli,Rs. 10727 - 13409,Rs. 17765 - 22440,Rs. 25500 - 31875
bangalore,Munnekollal,Rs. 9562 - 11156,Rs. 14960 - 17765,-
bangalore,Murugeshpalya,Rs. 12424 - 14494,Rs. 17118 - 20379,Rs. 20570 - 25245
bangalore,Nagavarapalya,-,Rs. 20272 - 21894,-
bangalore,Nagondanahalli,-,Rs. 12792 - 14620,-
bangalore,Nallurhalli,-,Rs. 17000 - 18700,Rs. 23143 - 25579
bangalore,New Thippasandra,Rs. 12464 - 14382,Rs. 20327 - 22175,-
bangalore,NRI Layout,-,Rs. 11475 - 14344,-
bangalore,Old Airport Road,-,Rs. 19907 - 23888,-
bangalore,Old Madras Road,-,Rs. 12840 - 15592,Rs. 17612 - 21386
bangalore,OMBR Layout,-,Rs. 17901 - 18896,-
bangalore,Outer Ring Road East,-,-,Rs. 34564 - 39073
bangalore,Pai Layout,-,Rs. 19074 - 19941,-
bangalore,Panathur,-,Rs. 20528 - 24990,Rs. 23273 - 25600
bangalore,Pattandur Agrahara,-,Rs. 19421 - 21270,-
bangalore,Puttappa Layout,-,Rs. 21212 - 23056,-
bangalore,Ramagondanahalli,-,Rs. 18008 - 19009,Rs. 27693 - 30770
bangalore,Ramamurthy Nagar,-,Rs. 12162 - 13030,-
bangalore,Sarjapur,-,-,-
bangalore,Sarjapur  Road,Rs. 10264 - 11495,Rs. 17765 - 22440,Rs. 25840 - 31280
bangalore,Sathya Layout,Rs. 11934 - 12818,-,-
bangalore,Seegehalli,-,Rs. 13090 - 14960,Rs. 19316 - 20604
bangalore,Seetharampalya,-,Rs. 18475 - 21114,-
bangalore,Silver Springs Layout,-,-,-
bangalore,Sompura,-,Rs. 9536 - 11003,Rs. 12607 - 15759
bangalore,Sonnenahalli,-,-,-
bangalore,TC Palaya,-,Rs. 12852 - 15606,-
bangalore,Thigalarapalya,-,-,Rs. 31492 - 33150
bangalore,Thubarahalli,-,-,Rs. 21038 - 25245
bangalore,Varthur,Rs. 7140 - 7140,Rs. 14416 - 16218,Rs. 16184 - 20808
bangalore,Varthur Road,-,Rs. 15129 - 17799,-
bangalore,Vasanth Nagar,-,-,-
bangalore,Vignana Nagar,Rs. 9962 - 12452,Rs. 14927 - 15805,Rs. 17850 - 19125
bangalore,Whitefield,-,Rs. 15852 - 20514,Rs. 21202 - 26503
bangalore,Yemlur,-,-,-
bangalore,Abbigere,-,Rs. 12559 - 13396,-
bangalore,Abshot Layout,-,Rs. 40424 - 46065,Rs. 57800 - 65025
bangalore,Amruthahalli,-,Rs. 12920 - 14535,-
bangalore,Ashirvad Colony,-,-,-
bangalore,Ashwathnagar,-,Rs. 11717 - 15623,-
bangalore,Avalahalli,-,-,-
bangalore,Babusapalaya,-,Rs. 14025 - 15895,-
bangalore,Budigere,-,Rs. 13872 - 14797,Rs. 16320 - 19040
bangalore,Chikkabanavar,-,Rs. 6487 - 8920,-
bangalore,Chokkanahalli,-,Rs. 17071 - 17969,Rs. 15326 - 20042
bangalore,Coconut Grove Layout,-,-,-
bangalore,Dasarahalli,-,Rs. 13090 - 14960,-
bangalore,Devanahalli,-,-,Rs. 11546 - 14433
bangalore,Devi Nagar,-,Rs. 12031 - 13750,-
bangalore,Doddaballapur,-,-,-
bangalore,Dollars Colony,-,-,Rs. 28900 - 34000
bangalore,Hebbal,-,Rs. 15341 - 19176,Rs. 24453 - 32094
bangalore,Hebbal Kempapura,-,Rs. 16320 - 20400,Rs. 32183 - 36571
bangalore,Hegde Nagar,-,Rs. 14810 - 16662,Rs. 23554 - 26324
bangalore,Hennur,Rs. 9575 - 12767,Rs. 15895 - 18700,Rs. 23338 - 29172
bangalore,Hennur Gardens,-,-,Rs. 21039 - 27614
bangalore,Hennur Road,Rs. 9358 - 12478,Rs. 15895 - 18700,Rs. 23120 - 27455
bangalore,Horamavu,-,Rs. 13399 - 16271,Rs. 15514 - 20288
bangalore,Horamavu Agara,-,Rs. 13090 - 15895,Rs. 18790 - 20132
bangalore,Horamavu Banaswadi,-,Rs. 13171 - 14049,-
bangalore,IVC Road,-,-,Rs. 11546 - 14433
bangalore,Jakkur,-,Rs. 16198 - 19235,-
bangalore,Jakkur Plantation,-,-,Rs. 35737 - 45060
bangalore,Jalahalli,-,Rs. 13872 - 15606,Rs. 19123 - 24587
bangalore,Jalahalli East,-,Rs. 10532 - 12036,Rs. 13007 - 14865
bangalore,Kanaka Nagar,-,-,Rs. 27425 - 34739
bangalore,Karthik Nagar,Rs. 11985 - 14382,-,-
bangalore,Kaval Byrasandra,-,Rs. 11220 - 14960,Rs. 18785 - 20995
bangalore,Kempapura,-,Rs. 14363 - 17441,-
bangalore,Kereguddadahalli,-,-,-
bangalore,Kodigehaali,-,Rs. 11503 - 14158,Rs. 17149 - 19435
bangalore,Kogilu,-,-,-
bangalore,Kothanur,-,Rs. 13090 - 15895,Rs. 20075 - 22943
bangalore,Malleshwaram,-,Rs. 25500 - 31620,Rs. 45363 - 48603
bangalore,Maruthi Sevanagar,-,Rs. 16320 - 18360,-
bangalore,Medahalli,-,Rs. 11900 - 13600,-
bangalore,Nagavara,-,Rs. 16430 - 19329,Rs. 31246 - 34371
bangalore,Nehru Nagar,-,-,-
bangalore,R.T. Nagar,-,Rs. 14662 - 16618,Rs. 20183 - 25565
bangalore,Rachenahalli,-,Rs. 14946 - 19617,Rs. 19992 - 25704
bangalore,Sadashiva Nagar,-,-,Rs. 62424 - 71604
bangalore,Sahakara Nagar,-,Rs. 13459 - 18266,Rs. 22338 - 28295
bangalore,Sanjay Nagar,-,-,Rs. 24480 - 29070
bangalore,Sultan Palaya,-,Rs. 14158 - 16812,-
bangalore,Thanisandra,-,Rs. 15837 - 18632,Rs. 23120 - 27455
bangalore,Vasanth Nagar,-,Rs. 39270 - 45815,Rs. 55069 - 63999
bangalore,Vidyaranyapura,-,Rs. 11067 - 13834,Rs. 13090 - 17850
bangalore,Yelahanka,-,Rs. 13899 - 17870,Rs. 16420 - 21473
bangalore,Yelahanka New Town,-,Rs. 10710 - 14280,Rs. 15470 - 20230
bangalore,Yeshwanthpur,-,Rs. 24477 - 27669,Rs. 32145 - 39451
chennai,Alapakkam,-,Rs. 6582 - 8228,-
chennai,Alwarthirunagar,-,Rs. 10200 - 12240,-
chennai,Arcot Road,Rs. 7521 - 8595,Rs. 12240 - 14535,Rs. 21314 - 27582
chennai,Ayappakkam,-,-,-
chennai,Chembarambakkam,-,Rs. 9518 - 10384,Rs. 16256 - 19508
chennai,Gerugambakkam,-,Rs. 8534 - 9387,-
chennai,Irungattukottai,-,Rs. 7473 - 8007,-
chennai,Iyyappanthangal,-,Rs. 7667 - 9758,-
chennai,Kattupakkam,-,-,-
chennai,Kolapakkam,-,Rs. 8583 - 10144,-
chennai,Koyambedu,-,Rs. 10115 - 13728,Rs. 14851 - 19094
chennai,Madanandapuram,-,Rs. 9180 - 10710,-
chennai,Maduravoyal,-,-,-
chennai,Mangadu,-,-,-
chennai,Mugalivakkam,-,Rs. 9945 - 12240,-
chennai,Nerkundram,-,Rs. 11269 - 12879,-
chennai,Poonamallee,-,-,Rs. 14219 - 17774
chennai,Porur,-,-,Rs. 19125 - 25500
chennai,Ramapuram,-,Rs. 12240 - 14535,Rs. 17468 - 19796
chennai,Saligramam,-,Rs. 13728 - 16958,Rs. 24905 - 27396
chennai,Sankareswarar Nagar,-,-,Rs. 24665 - 28029
chennai,Sriperumbudur,-,-,-
chennai,Thiruverkadu,-,Rs. 7480 - 8840,-
chennai,Valasaravakkam,-,Rs. 11475 - 13770,Rs. 17493 - 22491
chennai,Vanagaram,-,-,Rs. 13270 - 15482
chennai,Virugambakkam,-,Rs. 12282 - 15172,Rs. 21632 - 27994
chennai,Aminjikarai,-,Rs. 13600 - 16150,-
chennai,Anna Salai,-,-,Rs. 110500 - 125970
chennai,Arumbakkam,-,Rs. 13573 - 15269,Rs. 21236 - 25956
chennai,Athreya Puram,-,Rs. 13627 - 15331,-
chennai,Chetpet,-,-,Rs. 38611 - 50362
chennai,Choolaimedu,Rs. 8522 - 9942,Rs. 14450 - 17000,Rs. 19720 - 23418
chennai,Egmore,-,Rs. 20352 - 24776,Rs. 54251 - 65981
chennai,Kilpauk,-,Rs. 18700 - 22440,Rs. 28560 - 34000
chennai,Nelson Manickam Road,-,Rs. 16830 - 19635,Rs. 22440 - 25245
chennai,Nungambakkam,-,Rs. 16065 - 19635,-
chennai,Poes Garden,-,-,Rs. 117045 - 130815
chennai,Sowrashtra Nagar,-,Rs. 15300 - 18700,-
chennai,Sterling Road,-,Rs. 23154 - 26627,Rs. 34850 - 40078
chennai,Thiyagaraya Nagar,-,Rs. 16490 - 22262,Rs. 47280 - 62577
chennai,Triplicane,-,Rs. 14605 - 16596,-
chennai,Abhiramapuram,-,-,Rs. 45815 - 57269
chennai,Adambakkam,-,Rs. 10710 - 13005,-
chennai,Adyar,Rs. 12750 - 14790,Rs. 21250 - 25500,Rs. 42840 - 56610
chennai,Alandur,-,Rs. 16667 - 21053,Rs. 23035 - 28794
chennai,Alwarpet,-,Rs. 22100 - 28900,Rs. 60690 - 78540
chennai,Anakaputhur,-,-,-
chennai,Arasankazhani,-,Rs. 10774 - 12431,-
chennai,Ashok Nagar,-,Rs. 13770 - 16830,Rs. 24363 - 28662
chennai,Baby Nagar,-,Rs. 15042 - 16812,-
chennai,Besant Nagar,-,Rs. 22440 - 26180,Rs. 39270 - 47685
chennai,Bhuvaneshwari Nagar,-,Rs. 13005 - 15300,-
chennai,Boat Club,-,-,Rs. 121550 - 139230
chennai,Camp Road,Rs. 5189 - 6133,Rs. 8711 - 10163,-
chennai,Chettipunniyam,-,Rs. 9027 - 9779,-
chennai,Chitlapakkam,-,Rs. 8808 - 10409,-
chennai,Chromepet,Rs. 4675 - 6078,Rs. 7499 - 9544,-
chennai,East Tambaram,-,-,-
chennai,ECR,-,-,Rs. 30836 - 39246
chennai,Egattur,-,Rs. 17381 - 20278,-
chennai,Gopalapuram,-,-,-
chennai,Gowrivakkam,-,Rs. 8228 - 10472,-
chennai,GST Road,-,-,-
chennai,Guduvancheri,-,Rs. 6365 - 8486,-
chennai,Guindy,Rs. 7023 - 9501,Rs. 13728 - 17765,Rs. 19508 - 25245
chennai,Habibullah Road,-,Rs. 20359 - 22056,Rs. 33130 - 42792
chennai,Hastinapuram,-,-,-
chennai,Indira Nagar,-,-,Rs. 34574 - 41488
chennai,Jafferkhanpet,-,Rs. 11949 - 14605,-
chennai,K.K. Nagar,-,Rs. 12860 - 15130,Rs. 21509 - 27245
chennai,Kalakshetra Colony,-,Rs. 21016 - 24671,Rs. 40919 - 47974
chennai,Kamaraj Nagar,-,-,Rs. 22497 - 29601
chennai,Kandanchavadi,-,Rs. 11900 - 14875,-
chennai,Kandigai,-,-,-
chennai,Karapakkam,-,Rs. 12763 - 16166,Rs. 16052 - 17122
chennai,Kattankulathur,-,-,Rs. 15096 - 20757
chennai,Kazhipattur,-,Rs. 10310 - 11896,Rs. 12305 - 15660
chennai,Keelkattalai,-,Rs. 9823 - 12846,-
chennai,Kelambakkam,Rs. 5795 - 7865,-,Rs. 9180 - 11220
chennai,Kodambakkam,Rs. 6690 - 7871,Rs. 16371 - 18827,Rs. 23800 - 26180
chennai,Kotturpuram,-,Rs. 15300 - 18700,-
chennai,Kovilambakkam,-,Rs. 10200 - 11050,Rs. 17850 - 21420
chennai,Krishnapuri,-,-,Rs. 65057 - 67713
chennai,Kundrathur,-,Rs. 7098 - 9227,-
chennai,Madambakkam,-,Rs. 7160 - 9547,-
chennai,Madipakkam,-,Rs. 9394 - 11743,-
chennai,Mahindra City,-,Rs. 11587 - 13760,-
chennai,Mambakkam,Rs. 8078 - 9425,-,Rs. 12622 - 14918
chennai,Manapakkam,-,Rs. 12920 - 15342,-
chennai,Mandaveli,-,-,-
chennai,Manivakkam,-,-,-
chennai,Maraimalai Nagar,-,-,Rs. 15902 - 19877
chennai,Medavakkam,-,Rs. 9690 - 12112,Rs. 12641 - 16089
chennai,Mehta Nagar,-,-,-
chennai,MRC Nagar,-,Rs. 59310 - 78676,-
chennai,Mudichur,-,-,-
chennai,Mylapore,Rs. 8907 - 10604,-,-
chennai,Nallambakkam,-,-,-
chennai,Nanganallur,-,Rs. 10838 - 12282,-
chennai,Nanmangalam,-,Rs. 6800 - 8160,-
chennai,Navalur,Rs. 10445 - 11750,Rs. 13954 - 18314,Rs. 18003 - 21604
chennai,New Perungalathur,-,Rs. 6640 - 8854,-
chennai,Okkiyam Thuraipakkam,-,-,-
chennai,Old Perungalathur,-,-,-
chennai,OMR,-,Rs. 11602 - 14918,Rs. 15470 - 20230
chennai,Oragadam,-,Rs. 7097 - 8387,-
chennai,Padappai,-,Rs. 5738 - 7012,-
chennai,Padur,-,Rs. 11271 - 12138,Rs. 14165 - 18028
chennai,Palavakkam,Rs. 5610 - 7650,-,-
chennai,Pallavaram,Rs. 8752 - 11669,Rs. 10627 - 12145,Rs. 14365 - 17680
chennai,Pallikaranai,-,Rs. 12277 - 14165,Rs. 13483 - 17160
chennai,Pammal,-,Rs. 7718 - 10033,Rs. 12155 - 15470
chennai,Perumbakkam,-,Rs. 10973 - 12661,-
chennai,Perungalathur,-,Rs. 7268 - 9690,-
chennai,Perungudi,-,Rs. 14091 - 16440,Rs. 19244 - 24055
chennai,Potheri,-,-,-
chennai,Pudupakkam Village,Rs. 8854 - 10118,-,Rs. 7405 - 9051
chennai,Puzhuthivakkam,-,-,-
chennai,Radha Nagar,-,Rs. 7443 - 8796,-
chennai,Rajakilpakkam,-,Rs. 7994 - 9448,-
chennai,RA Puram,-,Rs. 21318 - 24871,Rs. 62475 - 83895
chennai,Revathipuram,-,Rs. 6472 - 7910,-
chennai,Saidapet,Rs. 6120 - 7650,-,-
chennai,Santhosapuram,-,-,-
chennai,Selaiyur,-,Rs. 8711 - 10163,-
chennai,Sembakkam,-,Rs. 7901 - 10056,-
chennai,Semmancheri,-,-,Rs. 15224 - 16746
chennai,Semmenchery,-,-,-
chennai,Shastri Nagar,-,-,Rs. 45055 - 50356
chennai,Sholinganallur,-,Rs. 14710 - 18171,Rs. 19679 - 23369
chennai,Singaperumal Koil,-,Rs. 8181 - 9669,-
chennai,Siruseri,Rs. 8123 - 10261,Rs. 8813 - 11016,Rs. 13399 - 17053
chennai,Sithalapakkam,-,Rs. 9180 - 10710,-
chennai,S Kolathur,-,-,-
chennai,Sunnambu Kolathur,-,-,-
chennai,T.Nagar,Rs. 8959 - 11199,Rs. 15137 - 18741,Rs. 31730 - 38627
chennai,Tambaram,Rs. 5437 - 6343,Rs. 8116 - 10329,Rs. 10557 - 13724
chennai,Tambaram Sanatoruim,-,-,-
chennai,Thaiyur,-,Rs. 5967 - 7344,-
chennai,Thalambur,-,-,-
chennai,Thirumudivakkam,-,Rs. 10163 - 12340,-
chennai,Thiruporur,-,-,Rs. 6991 - 8989
chennai,Thiruvanchery,-,-,-
chennai,Thiruvanmiyur,-,Rs. 17340 - 21675,Rs. 32492 - 39556
chennai,Thoraipakkam,-,Rs. 13682 - 16247,-
chennai,Trustpuram,-,Rs. 12112 - 14535,-
chennai,Ullagaram,-,-,-
chennai,Urapakkam,-,-,Rs. 9104 - 11835
chennai,Vandalur,-,-,-
chennai,Vandalur Kelambakkam Road,Rs. 8078 - 9874,-,Rs. 8499 - 10388
chennai,Varadarajapuram,-,-,-
chennai,Velachery,Rs. 7331 - 9775,Rs. 13151 - 15617,Rs. 18930 - 22270
chennai,Vengaivasal,-,-,-
chennai,Viduthalai Nagar,-,-,-
chennai,West Mambalam,-,Rs. 13102 - 14350,-
chennai,West Tambaram,-,-,Rs. 8583 - 11444
chennai,Zamin Pallavaram,-,Rs. 11156 - 12644,-
chennai,Ambattur,Rs. 5171 - 6033,Rs. 7948 - 10115,Rs. 11856 - 15089
chennai,Anna Nagar,-,Rs. 17000 - 22100,Rs. 32640 - 42160
chennai,Anna Nagar East,-,-,Rs. 30600 - 36975
chennai,Anna Nagar West,-,-,Rs. 37393 - 46022
chennai,Anna Nagar Western Extension,-,Rs. 15300 - 17595,-
chennai,Annanur,-,-,-
chennai,Avadi,-,Rs. 6792 - 8150,-
chennai,Ayanambakkam,-,-,-
chennai,Ayanavaram,-,Rs. 9991 - 12211,Rs. 24796 - 25923
chennai,Kallikuppam,-,-,-
chennai,Kodungaiyur,-,-,-
chennai,Kolathur,-,Rs. 9170 - 11462,-
chennai,Korattur,-,-,Rs. 19686 - 26248
chennai,Lakshmipuram,-,-,-
chennai,Madhavaram,-,-,-
chennai,Mogappair,-,-,-
chennai,Mogappair East,-,Rs. 11985 - 14382,-
chennai,Mogappair West,-,Rs. 10710 - 12240,Rs. 13315 - 17412
chennai,Nolambur,-,Rs. 11305 - 13728,Rs. 13423 - 15660
chennai,Paruthipet,-,-,-
chennai,Perambalur,-,Rs. 9960 - 12095,-
chennai,Perambur,Rs. 5610 - 7480,Rs. 9282 - 11424,Rs. 14045 - 18366
chennai,Purasaiwakkam,-,-,-
chennai,Shanthi Colony,-,Rs. 18582 - 22121,-
chennai,Thirumullaivoyal,-,Rs. 7225 - 8670,-
chennai,Villivakkam,Rs. 5516 - 6018,Rs. 9448 - 11628,-
hyderabad,3rd Phase KPHB,-,-,Rs. 22930 - 24363
hyderabad,5th Phase KPHB,-,-,Rs. 35493 - 43559
hyderabad,6th Phase KPHB,-,Rs. 13872 - 15606,-
hyderabad,A.S Rao Nagar,-,-,-
hyderabad,Adibatla,-,-,-
hyderabad,Alkapuri,-,-,-
hyderabad,Ameerpet,Rs. 5916 - 6409,Rs. 10047 - 11722,Rs. 15300 - 19125
hyderabad,Aminpur,-,Rs. 8296 - 10785,-
hyderabad,Anjaiah Nagar,Rs. 10540 - 11858,-,-
hyderabad,Attapur,-,Rs. 8500 - 11050,Rs. 13014 - 15616
hyderabad,Bachupally,-,Rs. 7480 - 8415,-
hyderabad,Bandam Kommu,-,-,Rs. 18850 - 21542
hyderabad,Bandlaguda,-,Rs. 8285 - 10126,-
hyderabad,Bangalore Highway,-,Rs. 21366 - 26115,-
hyderabad,Banjara Hills,Rs. 7714 - 9256,-,-
hyderabad,Beeramguda,-,-,-
hyderabad,Begumpet,Rs. 5100 - 6630,Rs. 10928 - 13450,Rs. 19762 - 23715
hyderabad,Boduppal,-,-,-
hyderabad,Chandanagar,-,Rs. 12661 - 14349,Rs. 15300 - 16575
hyderabad,D.D. Colony,-,Rs. 12974 - 13785,Rs. 18588 - 21243
hyderabad,Dilsukh Nagar,-,Rs. 7599 - 9119,-
hyderabad,Film Nagar,-,-,Rs. 25501 - 30869
hyderabad,Financial District,-,Rs. 21366 - 26115,-
hyderabad,Forest Department Colony,Rs. 8453 - 10442,Rs. 14387 - 16600,-
hyderabad,Gachibowli,-,-,-
hyderabad,Gajulramaram,-,-,-
hyderabad,Goutami Enclave,-,Rs. 13426 - 15491,-
hyderabad,Gouthami Enclave,Rs. 8255 - 9287,Rs. 14382 - 15341,-
hyderabad,Hafeezpet,-,Rs. 13846 - 16616,Rs. 19941 - 23929
hyderabad,Hi-Tech City,-,Rs. 18700 - 19635,Rs. 27423 - 33196
hyderabad,Himayat Nagar,-,-,Rs. 21420 - 26010
hyderabad,Hydershakote,-,-,-
hyderabad,Jubilee Hills,-,-,Rs. 29474 - 35679
hyderabad,Kapra,-,Rs. 6072 - 7590,-
hyderabad,Khajaguda,-,-,Rs. 25016 - 30574
hyderabad,Kokapet,-,-,Rs. 22236 - 25201
hyderabad,Kondapur,-,Rs. 14050 - 15924,Rs. 20808 - 26010
hyderabad,Kothaguda,-,-,Rs. 27948 - 33538
hyderabad,Kothapet,-,Rs. 8109 - 8920,-
hyderabad,KPHB,Rs. 4250 - 5525,Rs. 13423 - 17618,Rs. 23455 - 28667
hyderabad,Kukatpally,Rs. 7127 - 8772,-,Rs. 16464 - 20264
hyderabad,Laxmi Nagar,Rs. 7670 - 9588,Rs. 12724 - 16966,-
hyderabad,LB Nagar,-,Rs. 7650 - 9180,-
hyderabad,Lingampally,-,-,Rs. 16343 - 18857
hyderabad,Madhapur,Rs. 8058 - 10744,Rs. 16401 - 20260,Rs. 26010 - 31790
hyderabad,Madinaguda,-,-,Rs. 14492 - 15810
hyderabad,Manikonda,-,Rs. 13340 - 17151,-
hyderabad,Masjid Banda,-,-,Rs. 20182 - 25228
hyderabad,Mayuri Nagar,-,-,-
hyderabad,Mehdipatnam,-,Rs. 11555 - 14031,-
hyderabad,Miyapur,-,Rs. 10710 - 13388,Rs. 13529 - 17219
hyderabad,Moosapet,-,Rs. 12033 - 14810,-
hyderabad,Moti Nagar,-,-,-
hyderabad,Nagaram,-,-,-
hyderabad,Nagole,-,-,Rs. 8616 - 10770
hyderabad,Nallagandla,-,Rs. 15776 - 17748,Rs. 23596 - 26546
hyderabad,Nallakunta,-,-,Rs. 15647 - 16850
hyderabad,Nanakramguda,-,Rs. 20641 - 25405,-
hyderabad,Narsingi,-,-,Rs. 19125 - 24225
hyderabad,Neknampur,-,-,-
hyderabad,Nizampet,-,Rs. 10678 - 11648,Rs. 12223 - 15890
hyderabad,Patancheru Mandal,-,-,-
hyderabad,P Janardhan Reddy Nagar,-,-,-
hyderabad,Pocharam,-,Rs. 9670 - 11281,Rs. 11762 - 13901
hyderabad,Pragati Nagar,-,Rs. 9911 - 11713,Rs. 10940 - 13370
hyderabad,Puppalaguda,-,Rs. 12376 - 15232,-
hyderabad,Raghavendra Colony,Rs. 8541 - 10142,Rs. 14149 - 17181,Rs. 17128 - 21080
hyderabad,Rajarajeshwari Nagar,-,Rs. 13337 - 16415,-
hyderabad,Ramchandrapuram,-,-,Rs. 18945 - 21651
hyderabad,Sanath Nagar,-,Rs. 11155 - 13183,-
hyderabad,Sanjeeva Reddy Nagar,Rs. 6177 - 6177,Rs. 9782 - 11412,-
hyderabad,Serlingampally,-,-,Rs. 14531 - 19002
hyderabad,Shaikpet,-,Rs. 14960 - 15895,Rs. 21583 - 26979
hyderabad,Sindhi Colony,-,Rs. 12495 - 13536,-
hyderabad,Somajiguda,-,Rs. 11733 - 15086,Rs. 22794 - 27067
hyderabad,Srinagar Colony,-,-,Rs. 23120 - 27455
hyderabad,Telecom Nagar,-,Rs. 15470 - 19040,-
hyderabad,Tellapur,-,-,Rs. 10710 - 11900
hyderabad,Tolichowki,-,-,Rs. 13270 - 15482
hyderabad,Upparpally,-,-,Rs. 10962 - 14617
hyderabad,Vittal Rao Nagar,-,-,Rs. 35789 - 46015
hyderabad,Whitefield,-,-,Rs. 24480 - 29920
pune,Abasaheb Raikar Nagar,-,-,-
pune,Akurdi,Rs. 9180 - 10200,Rs. 12240 - 14535,-
pune,Alandi,Rs. 4675 - 5142,-,-
pune,Alandi Road,Rs. 5814 - 6783,Rs. 9702 - 11194,-
pune,Ambedkar Nagar,-,-,-
pune,Ambegaon,Rs. 6332 - 7793,Rs. 9119 - 11398,Rs. 13260 - 15470
pune,Ambegaon Bk,-,Rs. 8415 - 10710,-
pune,Ambegaon Budruk,Rs. 6310 - 8251,Rs. 9591 - 12543,-
pune,Ambegaon Pathar,-,-,-
pune,Anand Nagar,-,Rs. 11475 - 13770,-
pune,Ashoka Nagar,-,Rs. 20607 - 21544,Rs. 25526 - 26741
pune,Ashok Nagar,-,-,-
pune,Aundh,Rs. 11832 - 13311,Rs. 16660 - 19159,Rs. 23466 - 27171
pune,Aundh Gaon,Rs. 10883 - 12862,-,-
pune,B.T Kawade Road,Rs. 9945 - 12431,Rs. 15278 - 19298,-
pune,Bakori,Rs. 3243 - 3706,-,-
pune,Balaji Nagar,-,-,-
pune,Balewadi,Rs. 9690 - 12750,Rs. 15172 - 17850,Rs. 18564 - 22277
pune,Balewadi Phata,-,Rs. 16877 - 18653,Rs. 21080 - 25032
pune,Baner,Rs. 11220 - 12750,Rs. 15172 - 17850,Rs. 20400 - 24225
pune,Baner-Sus,-,Rs. 11983 - 14551,Rs. 14382 - 17978
pune,Baner Pashan Link Road,-,Rs. 15172 - 16958,Rs. 20400 - 22950
pune,Baramati,-,-,-
pune,Bavdhan,Rs. 8537 - 10909,Rs. 13600 - 15300,Rs. 16660 - 19040
pune,Benkar Nagar,Rs. 4845 - 5814,-,-
pune,Bhairav Nagar,Rs. 8415 - 9350,-,-
pune,Bhawani Peth,-,-,-
pune,Bhekrai Nagar,Rs. 6564 - 8078,-,Rs. 20305 - 25381
pune,Bhor,Rs. 3581 - 4558,Rs. 5692 - 6640,-
pune,Bhosale Nagar,-,Rs. 21509 - 23558,Rs. 26454 - 29238
pune,Bhosari,Rs. 7140 - 8670,Rs. 9392 - 11560,-
pune,Bhugaon,-,Rs. 10387 - 11985,-
pune,Bhujbal Vasti,-,Rs. 12699 - 15239,-
pune,Bhumkar Nagar,-,Rs. 13546 - 16085,Rs. 17493 - 19825
pune,Bhunde Vasti,-,Rs. 13328 - 14161,Rs. 14943 - 16188
pune,Bhusari Colony,Rs. 10353 - 11339,Rs. 16150 - 17850,Rs. 22950 - 26775
pune,Bibwewadi,Rs. 8752 - 11183,Rs. 12553 - 14906,-
pune,Bibwewadi Kondhwa Road,Rs. 9335 - 11300,Rs. 12920 - 15342,-
pune,Boat Club Road,-,-,Rs. 38366 - 42792
pune,Bopodi,-,Rs. 15300 - 17850,-
pune,Borhade Wadi,Rs. 6586 - 7092,Rs. 7420 - 9647,-
pune,Bund Garden,-,Rs. 22134 - 25296,-
pune,Camp,Rs. 11628 - 13082,-,-
pune,Chakan,Rs. 4752 - 5702,-,-
pune,Chandan Nagar,Rs. 9571 - 10528,Rs. 13600 - 16150,-
pune,Charholi,Rs. 5712 - 6664,Rs. 9724 - 11220,-
pune,Charholi Budruk,Rs. 4786 - 6221,-,-
pune,Chikhali,Rs. 5896 - 6878,Rs. 8466 - 9877,-
pune,Chinchwad,Rs. 8627 - 10149,Rs. 11475 - 14535,Rs. 20952 - 23418
pune,Chinchwad Gaon,Rs. 7915 - 8905,Rs. 11832 - 12572,-
pune,Chintamani Nagar,-,-,-
pune,Clover Park,Rs. 12376 - 14280,Rs. 21505 - 24310,-
pune,Dahanukar Colony,Rs. 10948 - 11900,Rs. 16065 - 18475,-
pune,Dange Chowk,Rs. 8350 - 10438,Rs. 12376 - 14144,-
pune,Dapodi,Rs. 8526 - 10030,Rs. 10460 - 12702,-
pune,Dashrath Nagar,-,-,Rs. 20305 - 25381
pune,Dattanagar,-,Rs. 10315 - 11690,-
pune,Dehu Road,-,-,-
pune,Dhankawadi,Rs. 7012 - 8415,Rs. 13505 - 14349,-
pune,Dhanori,Rs. 8526 - 10532,Rs. 12607 - 14183,Rs. 15988 - 17054
pune,Dhayari,Rs. 5330 - 6298,Rs. 7948 - 10115,-
pune,Dhayari Phata,Rs. 5320 - 6287,Rs. 9170 - 10698,-
pune,Dhole Patil Road,Rs. 13812 - 15938,Rs. 19380 - 24480,-
pune,Dighi,Rs. 7344 - 8323,Rs. 9525 - 11723,-
pune,Eon Free Zone,Rs. 11246 - 14994,Rs. 18742 - 21420,Rs. 21848 - 25704
pune,Erandwane,Rs. 11836 - 13730,Rs. 19550 - 21250,Rs. 28764 - 34756
pune,Fatima Nagar,Rs. 9350 - 10285,Rs. 14538 - 16356,Rs. 15470 - 20230
pune,Ganesh Nagar,-,-,-
pune,Ghorpadi,-,Rs. 16065 - 19125,-
pune,Gokul Nagar,-,-,-
pune,Hadapsar,-,Rs. 15940 - 19296,Rs. 22185 - 25882
pune,Hadapsar Gaon,Rs. 8135 - 10050,Rs. 13728 - 15342,-
pune,Handewadi,-,-,Rs. 14280 - 17850
pune,Hingne Khurd,Rs. 6243 - 8164,-,-
pune,Hinjewadi,Rs. 11046 - 13927,Rs. 14464 - 17868,Rs. 20794 - 24693
pune,Hinjewadi Phase 1,-,Rs. 16170 - 19202,Rs. 22903 - 26945
pune,Hinjewadi Phase 2,-,Rs. 17765 - 20570,-
pune,Jadhav Wadi,-,Rs. 8211 - 8895,-
pune,Jai Bhavani Nagar,Rs. 10547 - 12464,Rs. 15342 - 16958,-
pune,Jambhul,-,-,-
pune,Jambhulkar Mala,Rs. 8500 - 8925,-,-
pune,Kad Nagar,-,Rs. 10940 - 12622,-
pune,Kala Khadak,-,Rs. 13770 - 15606,-
pune,Kale Padal,Rs. 6688 - 8121,Rs. 10067 - 11506,-
pune,Kalewadi,Rs. 8813 - 9792,-,-
pune,Kalyani Nagar,Rs. 14586 - 16531,Rs. 23906 - 26775,Rs. 29920 - 36720
pune,Kalyani Nagar Annexe,Rs. 11587 - 13518,Rs. 19903 - 21798,Rs. 27846 - 31824
pune,Karve Nagar,Rs. 9350 - 11220,Rs. 16761 - 19156,Rs. 21558 - 26348
pune,Karve Road,-,Rs. 19550 - 21250,-
pune,Kasarwadi,-,-,-
pune,Kaspate Vasti,Rs. 10078 - 11669,Rs. 15389 - 17200,Rs. 17850 - 20400
pune,Kate Wasti,-,Rs. 9455 - 11819,-
pune,Kathepurna Nagar,Rs. 8160 - 9690,-,-
pune,Katraj,Rs. 5916 - 7888,Rs. 10746 - 13048,-
pune,Katraj Kondhwa Road,-,Rs. 10498 - 12920,Rs. 14382 - 17978
pune,Kedari Nagar,Rs. 10547 - 11506,Rs. 16150 - 18700,Rs. 19252 - 23103
pune,Keshav Nagar,-,Rs. 13728 - 15342,-
pune,Kesnand,-,-,-
pune,Khadki,-,-,-
pune,Kharadi,Rs. 10200 - 12750,Rs. 19224 - 21971,Rs. 28262 - 32725
pune,Kirkatwadi,-,Rs. 5975 - 6638,-
pune,Kiwale,Rs. 6630 - 8160,Rs. 9527 - 10321,-
pune,Kondhawe Dhawade,-,Rs. 6146 - 7375,-
pune,Kondhwa,Rs. 7711 - 9639,Rs. 11805 - 14334,Rs. 16188 - 19924
pune,Kondhwa Budruk,Rs. 6630 - 8840,Rs. 9078 - 10591,Rs. 12046 - 12046
pune,Koregaon Park,Rs. 17748 - 20213,Rs. 25497 - 33052,Rs. 33660 - 42075
pune,Koregaon Park Annexe,-,Rs. 22460 - 26204,Rs. 33680 - 39294
pune,Kothrud,Rs. 10174 - 12112,Rs. 17000 - 19550,Rs. 23970 - 26367
pune,Kunj Colony,-,Rs. 14713 - 18584,-
pune,Kutwal Colony,-,Rs. 12124 - 12837,-
pune,Law College Road,-,Rs. 24973 - 25934,Rs. 32640 - 35360
pune,Laxman Nagar,-,Rs. 17765 - 18700,Rs. 25245 - 26507
pune,Lohegaon,Rs. 6120 - 8160,Rs. 11373 - 12889,-
pune,Lokmanya Colony,Rs. 10353 - 11832,-,-
pune,Loni Kalbhor,-,-,-
pune,Lullanagar,Rs. 8568 - 9520,Rs. 14497 - 16430,-
pune,Madhav Nagar,Rs. 9945 - 10940,Rs. 12675 - 14260,-
pune,Magarpatta,Rs. 12818 - 14790,Rs. 18326 - 20825,Rs. 25891 - 31069
pune,Mahadev Nagar,-,-,-
pune,Mahalunge,Rs. 7548 - 8963,Rs. 8284 - 11296,-
pune,Mahalunge Ingale,-,-,-
pune,Malwadi,-,Rs. 13150 - 14696,-
pune,Mamurdi,-,Rs. 9023 - 10663,-
pune,Manik Baug,-,Rs. 10710 - 12240,-
pune,Manjari Budruk,-,Rs. 9415 - 11587,-
pune,Manjri,Rs. 7586 - 9104,Rs. 11067 - 12648,Rs. 13445 - 17112
pune,Manjri BK,-,Rs. 10398 - 13597,Rs. 12740 - 15925
pune,Market Yard,Rs. 10835 - 12383,Rs. 15407 - 17840,-
pune,Marunji,Rs. 6497 - 8354,Rs. 10468 - 12561,-
pune,Marutirao Gaikwad Nagar,Rs. 11985 - 12944,-,-
pune,Mate Nagar,Rs. 8395 - 10371,-,-
pune,Mayur Colony,Rs. 10752 - 13090,Rs. 17765 - 20570,-
pune,Meera Nagar,-,Rs. 30408 - 39236,Rs. 36720 - 43520
pune,Meeta Nagar,-,-,-
pune,Mhada Colony,Rs. 13770 - 15810,Rs. 22419 - 25109,Rs. 27882 - 31684
pune,Mhasoba Nagar,-,Rs. 16218 - 17029,-
pune,Model Colony,Rs. 14586 - 16045,-,-
pune,Mohamadwadi,-,Rs. 11536 - 14198,Rs. 15504 - 19380
pune,Mokarwadi,Rs. 5236 - 5712,Rs. 7225 - 9392,-
pune,Morwadi,-,Rs. 13728 - 16150,-
pune,Moshi,Rs. 6586 - 7599,Rs. 7910 - 9348,Rs. 11631 - 12689
pune,Mundhwa,-,Rs. 13944 - 17225,-
pune,Nagar Road,Rs. 9282 - 10166,-,-
pune,Nanded,Rs. 8002 - 8446,Rs. 10221 - 11794,-
pune,Nandel Fata,-,-,-
pune,Narhe,Rs. 5236 - 5712,Rs. 7225 - 9392,-
pune,Nehru Nagar,-,-,-
pune,Nere,Rs. 3581 - 4558,Rs. 5692 - 6640,-
pune,New Sanghvi,Rs. 8670 - 10200,Rs. 11601 - 14501,-
pune,NIBM,Rs. 9042 - 10549,Rs. 11415 - 14049,Rs. 16575 - 19125
pune,Nigdi,Rs. 8160 - 10200,Rs. 12186 - 13709,-
pune,North Hadapsar,Rs. 12431 - 12928,Rs. 14596 - 16218,-
pune,Old Sangvi,Rs. 8410 - 9894,Rs. 11876 - 15269,-
pune,Padmavati,-,-,-
pune,Pandhari Nagar,-,Rs. 16432 - 17345,-
pune,Pandurang Industrial Area,Rs. 8247 - 8705,Rs. 10033 - 11577,Rs. 11262 - 13515
pune,Parkhe Vasti,Rs. 10772 - 12177,Rs. 13296 - 15512,-
pune,Pashan,Rs. 9588 - 11506,Rs. 13600 - 16150,Rs. 17697 - 21236
pune,Pashan-Sus Road,Rs. 10251 - 11276,Rs. 13728 - 15342,Rs. 17576 - 20087
pune,Patil Nagar,Rs. 8595 - 10744,Rs. 13736 - 15453,Rs. 15525 - 19108
pune,Paud Road,Rs. 11730 - 13260,Rs. 18700 - 20400,-
pune,Phase-3 Hinjewadi,-,Rs. 12699 - 16085,-
pune,Phursungi,-,Rs. 10276 - 11858,-
pune,Pimple Gurav,Rs. 8670 - 10710,Rs. 13106 - 14648,Rs. 15938 - 19125
pune,Pimple Nilakh,Rs. 9625 - 11652,Rs. 12961 - 15391,Rs. 28085 - 36954
pune,Pimple Saudagar,Rs. 10960 - 13048,Rs. 15300 - 17000,Rs. 19040 - 21420
pune,Pimpri,Rs. 9180 - 11730,Rs. 14450 - 17000,Rs. 20952 - 22185
pune,Pimpri Chinchwad,Rs. 8160 - 10200,Rs. 12750 - 14450,Rs. 16660 - 20230
pune,Pingale Wasti,-,Rs. 19462 - 22705,-
pune,Pirangut,Rs. 4552 - 5058,Rs. 6564 - 7293,-
pune,Pisoli,-,Rs. 8304 - 9965,-
pune,Postal Colony,Rs. 8721 - 11144,Rs. 14450 - 16150,-
pune,Prabhat Road,-,-,-
pune,Pradhikaran,-,Rs. 11475 - 13770,-
pune,Prasad Nagar,Rs. 9588 - 10547,-,-
pune,Punawale,Rs. 7778 - 8296,Rs. 10951 - 12635,Rs. 14484 - 16898
pune,Pune-Satara Road,Rs. 8675 - 10121,Rs. 12553 - 14906,-
pune,Pune Mumbai Highway,Rs. 10557 - 11085,Rs. 16062 - 20077,Rs. 24453 - 25981
pune,Pune Nagar Road,Rs. 4811 - 5292,Rs. 5780 - 7225,-
pune,Pune Sholapur Road,Rs. 3930 - 4913,-,-
pune,Rahatani,Rs. 9333 - 11407,Rs. 13437 - 15956,Rs. 18488 - 22185
pune,Rajashri Colony,Rs. 7714 - 9256,-,-
pune,Rajgurunagar,-,-,-
pune,Rakshak Nagar,-,Rs. 14229 - 15810,-
pune,Rambaug Colony,Rs. 11220 - 12155,Rs. 19550 - 22950,-
pune,Ramkrishna Paramhans Nagar,Rs. 9996 - 11424,Rs. 15592 - 19260,-
pune,Rasta Peth,-,-,-
pune,Ravet,Rs. 7778 - 9333,Rs. 11162 - 12757,Rs. 14875 - 18062
pune,Sadashiv Peth,Rs. 13260 - 17850,Rs. 19380 - 20188,-
pune,Sainath Nagar,-,Rs. 15407 - 17029,-
pune,Sainikwadi,-,Rs. 20290 - 23056,-
pune,Sakal Nagar,Rs. 11492 - 13702,-,-
pune,Sakore Nagar,Rs. 14280 - 15810,Rs. 18887 - 21462,Rs. 24089 - 25293
pune,Salisbury Park,-,Rs. 16218 - 18651,-
pune,Salunke Vihar,-,Rs. 14810 - 16662,-
pune,Samarth Colony,-,-,-
pune,Sanaswadi,-,-,-
pune,Sanewadi,Rs. 12243 - 13185,Rs. 16958 - 18572,Rs. 21925 - 28015
pune,Sant Nagar,-,-,-
pune,Sasane Nagar,Rs. 6902 - 8381,Rs. 10163 - 12340,-
pune,Satar Nagar,-,Rs. 9459 - 10186,-
pune,Satav Nagar,-,-,-
pune,Satavwadi,Rs. 8609 - 10761,-,-
pune,Sector-6 Moshi,-,-,-
pune,Sector-29 Ravet,-,Rs. 11105 - 12586,-
pune,Sector No-26 Pradhikaran,-,Rs. 11067 - 13280,-
pune,Senapati Bapat Road,-,Rs. 21250 - 24650,-
pune,Shaniwar Peth,Rs. 13447 - 13927,-,-
pune,Shankar Kalat Nagar,Rs. 10710 - 12750,Rs. 14999 - 16764,Rs. 19125 - 20400
pune,Shastri Nagar,Rs. 14256 - 16802,Rs. 19746 - 24038,-
pune,Shewalewadi,Rs. 6842 - 8309,-,-
pune,Shikrapur,-,-,-
pune,Shikshaknagar,Rs. 9925 - 11342,-,-
pune,Shivaji Nagar,-,-,-
pune,Shivane,Rs. 4598 - 5978,Rs. 8565 - 10900,-
pune,Shivneri Nagar,Rs. 9350 - 9818,-,-
pune,Shivtirth Nagar,Rs. 11033 - 13540,Rs. 14450 - 19550,-
pune,Siddartha Nagar,-,Rs. 14229 - 15810,-
pune,Siddharth Nagar,-,Rs. 14198 - 17354,-
pune,Sinhgad Road,Rs. 5273 - 6712,Rs. 8935 - 10424,Rs. 13117 - 15303
pune,Somatane,-,Rs. 6038 - 8303,-
pune,Somatne Phata,-,-,-
pune,Someshwarwadi,-,-,-
pune,Somnath Nagar,Rs. 8670 - 10710,-,-
pune,Sopan Baug,-,-,Rs. 26874 - 31117
pune,Sukhsagar Nagar,-,Rs. 10305 - 11778,-
pune,Sunita Nagar,Rs. 8338 - 10790,-,-
pune,Sus,-,Rs. 11829 - 14363,Rs. 13505 - 16881
pune,Sutarwadi,-,Rs. 13260 - 14918,-
pune,Swatantrya Sainik Nagar,-,Rs. 19380 - 20995,Rs. 22780 - 25058
pune,Talawade,-,-,-
pune,Talegaon,Rs. 4223 - 5278,-,-
pune,Talegaon Dabhade,Rs. 4752 - 5227,Rs. 5807 - 7259,-
pune,Talegaon Dhamdhere,-,-,-
pune,Tathawade,Rs. 7778 - 10370,Rs. 12281 - 14035,-
pune,Thergaon,Rs. 10207 - 11281,Rs. 13328 - 14994,-
pune,Thite Nagar,Rs. 8675 - 11567,Rs. 16328 - 18906,-
pune,Tilekar Nagar,-,Rs. 8041 - 8772,-
pune,Tilekar Vasti,-,Rs. 16150 - 17000,-
pune,Tingre Nagar,Rs. 10047 - 11554,Rs. 14535 - 17765,Rs. 21129 - 24651
pune,Tukaram Nagar,Rs. 10659 - 12903,Rs. 18885 - 20684,-
pune,Tulaja Bhawani Nagar,-,Rs. 18796 - 21481,-
pune,Ubale Nagar,Rs. 7012 - 9818,Rs. 11138 - 13525,-
pune,Udyog Nagar,-,Rs. 12151 - 12961,-
pune,Undri,Rs. 6564 - 8078,Rs. 8882 - 10498,Rs. 14025 - 17850
pune,Vadgaon Budruk,Rs. 6232 - 7670,Rs. 7948 - 10115,-
pune,Vadgaon Sheri,-,Rs. 17000 - 21250,Rs. 26180 - 27370
pune,Varale,-,Rs. 5379 - 6724,-
pune,Vasant Kunj,-,-,-
pune,Veerbhadra Nagar,-,Rs. 17000 - 18700,Rs. 17850 - 20230
pune,Vikas Nagar,-,Rs. 10111 - 10888,-
pune,Viman Nagar,Rs. 13701 - 15731,Rs. 20743 - 24350,Rs. 28050 - 33150
pune,Vishal Nagar,-,Rs. 13280 - 14756,-
pune,Vishnu Dev Nagar,-,-,-
pune,Vishrantwadi,Rs. 9746 - 11602,Rs. 15300 - 18700,Rs. 21420 - 24990
pune,Wadgaon Budruk,-,-,-
pune,Wadgaon Sheri,Rs. 9180 - 10710,Rs. 13728 - 16150,Rs. 22568 - 30090
pune,Wadmukhwadi,Rs. 6120 - 7650,-,-
pune,Wagholi,Rs. 6212 - 7247,Rs. 8817 - 9619,Rs. 11628 - 13954
pune,Wakad,Rs. 10336 - 11886,Rs. 14594 - 17170,Rs. 18232 - 21879
pune,Wakadkar Wasti,-,Rs. 15833 - 18095,-
pune,Wanowrie,Rs. 9710 - 11098,Rs. 16356 - 18173,Rs. 20590 - 23164
pune,Wanwadi,Rs. 9189 - 11124,Rs. 14280 - 16958,Rs. 22185 - 23418
pune,Warje,Rs. 8150 - 9588,Rs. 11985 - 13583,Rs. 16720 - 19108
pune,Warje Malwadi,-,-,-
pune,Wireless Colony,Rs. 12240 - 13770,Rs. 17136 - 19584,-
pune,Yamuna Nagar,-,Rs. 9520 - 11560,-
pune,Yerwada,Rs. 10832 - 12638,Rs. 16065 - 20081,Rs. 22865 - 24008
pune,Yewalewadi,Rs. 6111 - 7051,Rs. 8670 - 10115,-
kolkata,Entally,-,-,-
kolkata,Park Street,-,Rs. 39270 - 47685,-
kolkata,Sealdah,-,-,Rs. 32222 - 34700
kolkata,Andul,-,-,-
kolkata,Andul Road,-,-,-
kolkata,Bally,-,-,-
kolkata,Bhadrakali,-,-,-
kolkata,Chandannagar,-,-,-
kolkata,Chinsurah,-,-,-
kolkata,Hooghly,-,-,-
kolkata,Howrah,-,Rs. 11773 - 13013,Rs. 17253 - 20298
kolkata,Konnagar,-,Rs. 4980 - 6640,-
kolkata,Liluah,-,-,-
kolkata,Mankundu,-,-,-
kolkata,Rishra,-,-,-
kolkata,Santragachi,-,-,-
kolkata,Shibpur,-,-,-
kolkata,Uttarpara,-,-,-
kolkata,Action Area 1A,-,Rs. 11411 - 13694,Rs. 15122 - 17138
kolkata,Action Area 1B,-,-,Rs. 15360 - 17722
kolkata,Action Area 1C,-,-,Rs. 14365 - 16575
kolkata,Action Area 1D,-,-,Rs. 15768 - 18020
kolkata,Action Area I,-,Rs. 12559 - 15070,Rs. 14911 - 18106
kolkata,Action Area II,-,Rs. 12102 - 14792,Rs. 17340 - 19380
kolkata,Action Area IIB,-,Rs. 7568 - 8199,Rs. 13408 - 14627
kolkata,Action Area IIC,-,-,-
kolkata,Action Area III,Rs. 5603 - 5953,-,Rs. 12776 - 15331
kolkata,Bablatala,-,Rs. 7714 - 10519,-
kolkata,Chinar Park,Rs. 4962 - 5671,Rs. 8060 - 9525,Rs. 11398 - 13470
kolkata,Chingrighata,-,-,-
kolkata,City Centre 2,Rs. 6681 - 7349,Rs. 10780 - 13316,-
kolkata,Dash Drone,-,Rs. 9058 - 11322,-
kolkata,E M Bypass,-,-,Rs. 26180 - 30940
kolkata,Krishnapur,-,-,-
kolkata,Majarhati,-,-,-
kolkata,New Town,Rs. 6502 - 8309,Rs. 10159 - 12699,Rs. 15208 - 18467
kolkata,Rajarhat,Rs. 5046 - 6127,-,Rs. 11781 - 13744
kolkata,Salua,-,-,-
kolkata,Tangra,-,Rs. 17850 - 21250,Rs. 22100 - 25415
kolkata,Uniworld City,-,-,Rs. 20846 - 25016
kolkata,VIP Haldirams,-,Rs. 9401 - 10072,-
kolkata,Ajay Nagar,-,Rs. 12485 - 16386,-
kolkata,Alipore,-,-,-
kolkata,Bagha Jatin,-,Rs. 7948 - 10115,-
kolkata,Ballygunge,-,Rs. 23006 - 27430,-
kolkata,Ballygunge Circular Road,-,-,Rs. 58182 - 70762
kolkata,Bansdroni,-,Rs. 10341 - 13296,-
kolkata,Baruipur,-,-,-
kolkata,BataNagar,-,-,-
kolkata,Behala,-,Rs. 8398 - 9690,Rs. 14030 - 17037
kolkata,Behala Chowrasta,-,Rs. 8191 - 10238,Rs. 10210 - 12763
kolkata,Bhawanipore,-,-,-
kolkata,Bijoygarh,-,-,-
kolkata,B L Saha Road,-,-,Rs. 20606 - 22398
kolkata,Boral,-,-,-
kolkata,Brahmapur,-,-,-
kolkata,Dhakuria,-,Rs. 9901 - 12376,-
kolkata,E M Bypass,Rs. 10557 - 11339,Rs. 15744 - 18742,Rs. 30762 - 36354
kolkata,E M Bypass Extension,-,Rs. 7790 - 8989,Rs. 11271 - 13150
kolkata,Ganguly Bagan,-,-,-
kolkata,Garfa,-,-,-
kolkata,Garia,-,Rs. 8696 - 11372,Rs. 14042 - 17051
kolkata,Gariahat,-,Rs. 21503 - 24812,Rs. 29134 - 36126
kolkata,Golf Green,-,-,Rs. 16371 - 20009
kolkata,Haltu,-,-,-
kolkata,Haridebpur,-,-,-
kolkata,Hazra Road,-,-,Rs. 25500 - 32640
kolkata,Hiland Park,-,-,Rs. 18513 - 24684
kolkata,Jadavpur,-,Rs. 13495 - 16493,-
kolkata,Jodhpur Garden,-,Rs. 10498 - 12708,-
kolkata,Jodhpur Park,-,Rs. 20528 - 23205,Rs. 24098 - 28688
kolkata,Joka,-,-,-
kolkata,Kalighat,-,-,-
kolkata,Kalikapur,-,Rs. 9841 - 10544,-
kolkata,Kamalgazi,-,-,Rs. 11863 - 13840
kolkata,Kasba,Rs. 6430 - 7943,Rs. 11704 - 13770,Rs. 15150 - 18938
kolkata,Kudgat,-,-,-
kolkata,Lake Gardens,-,Rs. 13728 - 15895,Rs. 19768 - 24160
kolkata,Madurdaha,-,Rs. 10353 - 12572,Rs. 13376 - 15286
kolkata,Mahamayatala,-,-,-
kolkata,Maheshtala,-,Rs. 6707 - 8255,Rs. 10004 - 13006
kolkata,Mukundapur,-,Rs. 13600 - 17680,-
kolkata,Naktala,-,Rs. 9080 - 11025,-
kolkata,Narendrapur,-,Rs. 8718 - 11401,Rs. 10588 - 13234
kolkata,Nayabad,-,-,Rs. 9818 - 12495
kolkata,Netaji Nagar,-,-,-
kolkata,New Alipore,Rs. 8711 - 11614,Rs. 12684 - 14798,Rs. 21437 - 26796
kolkata,New Ballygunge,-,-,-
kolkata,New Garia,-,-,-
kolkata,Pailan,-,-,-
kolkata,Panchasayar,-,-,-
kolkata,Park Circus,-,-,-
kolkata,Parnasree Palli,-,-,-
kolkata,Patuli,-,Rs. 10258 - 13189,-
kolkata,Picnic Garden,-,Rs. 9588 - 10866,-
kolkata,Prince Anwar Shah Rd.,-,-,Rs. 34343 - 41703
kolkata,Prince Anwar Shah Road Connector,-,Rs. 10968 - 13548,-
kolkata,Purbalok,-,-,-
kolkata,Rajpur,-,-,Rs. 9170 - 11462
kolkata,Ranikuthi,-,Rs. 7735 - 10498,-
kolkata,Sakher Bazar,-,Rs. 8272 - 9651,-
kolkata,Santoshpur,-,-,-
kolkata,Sarsuna,-,Rs. 9271 - 11410,-
kolkata,Shibrampur,-,-,-
kolkata,Silpara,-,-,-
kolkata,Sonarpur,-,-,-
kolkata,Southern Avenue,-,-,Rs. 39440 - 46240
kolkata,Tagore Park,-,-,-
kolkata,Thakurpukur,-,-,Rs. 11857 - 12769
kolkata,Tollygunge,Rs. 6286 - 7765,-,Rs. 19110 - 23356
kolkata,Topsia,-,-,-
kolkata,Uttar Panchanna Gram,Rs. 5419 - 7012,-,-
kolkata,Vip Nagar,Rs. 5100 - 6375,-,-
kolkata,Agarpara,-,-,-
kolkata,Airport,-,Rs. 7640 - 8276,-
kolkata,Ariadaha,-,-,-
kolkata,Baguihati,Rs. 4835 - 6446,Rs. 6760 - 8604,-
kolkata,Bangur,-,-,-
kolkata,Bara Nagar,-,-,-
kolkata,Barasat,-,Rs. 5485 - 6704,-
kolkata,Barrackpore,-,-,-
kolkata,Belgharia,-,Rs. 5967 - 7956,-
kolkata,Belgharia Expressway,-,-,-
kolkata,Beliaghata,-,-,-
kolkata,Birati,-,Rs. 6588 - 8564,-
kolkata,B T Road,-,-,Rs. 13066 - 15866
kolkata,Dum Dum,-,Rs. 7480 - 9520,Rs. 11271 - 14089
kolkata,Dum Dum Cantt.,-,Rs. 5745 - 6384,-
kolkata,Dum Dum Park,-,Rs. 10532 - 12036,-
kolkata,Dunlop,-,-,-
kolkata,Durganagar,-,-,-
kolkata,H B Town,-,-,-
kolkata,Jessore Road,-,Rs. 10765 - 13932,-
kolkata,Jyangra,-,-,-
kolkata,Kadapara,-,-,-
kolkata,Kaikhali,-,Rs. 8011 - 9860,Rs. 13090 - 14025
kolkata,Kalyani,-,-,-
kolkata,Kankurgachi,-,-,Rs. 28856 - 35129
kolkata,Kestopur,Rs. 4752 - 5848,Rs. 7721 - 8365,Rs. 10526 - 11404
kolkata,Khardah,-,Rs. 6021 - 7358,-
kolkata,Lake Town,-,Rs. 10115 - 13005,Rs. 14025 - 17765
kolkata,Madhyamgram,-,Rs. 5898 - 7209,Rs. 7650 - 8500
kolkata,Maniktala,-,-,-
kolkata,Nager Bazar,-,Rs. 8730 - 10072,Rs. 11057 - 11978
kolkata,Narayanpur,-,-,-
kolkata,New Barrakpur,-,-,-
kolkata,Paikpara,-,-,-
kolkata,Phoolbagan,-,-,-
kolkata,Raghunathpur,-,-,-
kolkata,Rajbari,-,-,-
kolkata,Salt Lake,-,Rs. 11560 - 15172,Rs. 16294 - 19916
kolkata,Sector I - Salt Lake,-,-,Rs. 23418 - 28348
kolkata,Sector II - Salt Lake,-,Rs. 13005 - 15172,Rs. 17658 - 20774
kolkata,Sector III - Salt Lake,-,-,Rs. 18850 - 23038
kolkata,Sinthee,-,-,-
kolkata,Sodepur,-,Rs. 5440 - 6800,Rs. 8530 - 9478
kolkata,Teghoria,-,Rs. 8660 - 11546,-
kolkata,Ultadanga,-,-,-
kolkata,VIP Haldiram,-,Rs. 10332 - 13511,-
kolkata,Zarda Bagan,-,-,-
ahmedabad,Ambawadi,-,Rs. 12470 - 16626,Rs. 22950 - 29070
ahmedabad,Bodakdev,-,Rs. 13196 - 16715,Rs. 21379 - 26724
ahmedabad,C.G. Road,-,-,Rs. 23842 - 28050
ahmedabad,Drive In Road,-,Rs. 13438 - 16126,-
ahmedabad,Ghatlodia,Rs. 6436 - 7509,Rs. 8721 - 10465,-
ahmedabad,Gurukul,-,Rs. 13209 - 15851,-
ahmedabad,Jivraj Park,-,-,-
ahmedabad,Jodhpur,Rs. 7140 - 8925,Rs. 12453 - 16285,Rs. 19730 - 25367
ahmedabad,Judges Bunglow,-,-,-
ahmedabad,Juhapura,-,-,-
ahmedabad,Memnagar,-,Rs. 12750 - 15300,-
ahmedabad,Naranpura,-,Rs. 11669 - 14362,-
ahmedabad,Nava Vadaj,-,-,-
ahmedabad,Navrangpura,-,-,Rs. 19278 - 24786
ahmedabad,New Ranip,-,Rs. 7398 - 9041,-
ahmedabad,Nirnay Nagar,-,-,-
ahmedabad,Paldi,-,-,-
ahmedabad,Prernatirth Derasar Road,-,-,Rs. 20346 - 22889
ahmedabad,Ramdev Nagar,-,Rs. 13438 - 16126,-
ahmedabad,Ranip,-,-,-
ahmedabad,Satadhar,-,Rs. 10145 - 11067,-
ahmedabad,Satellite,-,Rs. 12708 - 16618,Rs. 19576 - 25168
ahmedabad,Satellite Extension,-,-,Rs. 18012 - 23554
ahmedabad,Shyamal Cross Road,-,-,Rs. 18742 - 21420
ahmedabad,Vasna,Rs. 5926 - 7902,-,-
ahmedabad,Vastrapur,-,Rs. 14688 - 18360,Rs. 19508 - 26010
ahmedabad,Vejalpur,Rs. 8119 - 10656,Rs. 11934 - 13770,Rs. 14260 - 15448
ahmedabad,Ghodasar,-,-,-
ahmedabad,Hathijan,-,-,-
ahmedabad,Isanpur,-,-,-
ahmedabad,Kankaria,-,-,-
ahmedabad,Maninagar,Rs. 6747 - 8193,Rs. 11016 - 12852,Rs. 17536 - 20234
ahmedabad,Maninagar East,-,Rs. 10603 - 12118,-
ahmedabad,Meghani Nagar,-,-,-
ahmedabad,Naroda,-,Rs. 4590 - 5355,-
ahmedabad,Narol,-,-,-
ahmedabad,Narolgam,-,-,-
ahmedabad,Nava Naroda,-,-,-
ahmedabad,New Maninagar,-,-,-
ahmedabad,Nikol,-,-,-
ahmedabad,Nikol - Naroda Road,-,-,-
ahmedabad,Odhav,-,-,-
ahmedabad,Shahibaug,-,-,Rs. 18266 - 23886
ahmedabad,Uttamnagar,-,Rs. 10098 - 11934,-
ahmedabad,Vastral,-,-,-
ahmedabad,Vatva,-,-,-
ahmedabad,Vinzol,-,-,-
ahmedabad,Ambli,-,-,-
ahmedabad,Ambli Bopal,-,-,-
ahmedabad,Bopal,-,Rs. 9668 - 12305,Rs. 20825 - 26775
ahmedabad,Chandlodia,-,-,-
ahmedabad,Ghuma,-,Rs. 9350 - 11050,-
ahmedabad,Gota,-,Rs. 8354 - 10210,Rs. 11092 - 13558
ahmedabad,Iscon-Ambli Road,-,-,-
ahmedabad,Jagatpur,Rs. 6350 - 6773,Rs. 8500 - 10200,Rs. 10480 - 12810
ahmedabad,Makarba,-,Rs. 13477 - 17071,-
ahmedabad,Prahlad Nagar,-,Rs. 13661 - 17564,Rs. 23174 - 27520
ahmedabad,Sarkhej,-,-,-
ahmedabad,Science City,-,Rs. 11730 - 13685,Rs. 14875 - 17850
ahmedabad,SG Highway,-,Rs. 10014 - 12745,-
ahmedabad,Shela,-,Rs. 11043 - 13410,Rs. 15525 - 16720
ahmedabad,Shilaj,-,Rs. 10365 - 12757,Rs. 12271 - 14316
ahmedabad,Sola,-,Rs. 11628 - 12597,Rs. 13410 - 16391
ahmedabad,South Bopal,-,Rs. 12174 - 14782,Rs. 13978 - 17204
ahmedabad,Thaltej,-,Rs. 13349 - 16019,Rs. 20349 - 26163
ahmedabad,Tragad,-,-,Rs. 9105 - 11382
ahmedabad,Vaishnodevi Circle,-,Rs. 9350 - 11050,Rs. 12410 - 16133
ahmedabad,Chandkheda,-,-,Rs. 13005 - 16906
ahmedabad,Gandhi Nagar,-,-,-
ahmedabad,Koteshwar,-,Rs. 7541 - 9426,-
ahmedabad,Kudasan,-,-,-
ahmedabad,Motera,-,Rs. 8231 - 10975,Rs. 13676 - 17779
ahmedabad,New CG Road,-,-,Rs. 13005 - 16906
ahmedabad,Sabarmati,-,-,-
ahmedabad,Sardar Patel Ring Road,-,-,Rs. 14863 - 19110
ahmedabad,Sargasan,-,-,-
ahmedabad,Sughad,-,-,-
ahmedabad,Vadsar,-,-,-
ahmedabad,Zundal,-,-,-
bhubaneswar,Dumduma,-,-,-
bhubaneswar,Ghatikia,-,-,-
bhubaneswar,Gothapatna,-,-,-
bhubaneswar,Hanspal,-,-,-
bhubaneswar,Kalinganagar,-,Rs. 8288 - 10774,-
bhubaneswar,Khandagiri,-,-,-
bhubaneswar,Nayapalli,-,-,-
bhubaneswar,Patia,-,Rs. 7997 - 9996,-
bhubaneswar,Patrapada,-,-,-
bhubaneswar,Raghunathpur,-,-,-
bhubaneswar,Sailashree Vihar,-,-,-
bhubaneswar,Sundarpada,-,Rs. 4131 - 4957,-
bhubaneswar,Tamando,-,-,-
coimbatore,Ganapathy,-,Rs. 8177 - 10630,-
coimbatore,Peelamedu,-,Rs. 12243 - 14127,-
coimbatore,Race Course,-,-,-
coimbatore,Ramanathapuram,-,Rs. 11503 - 12388,-
coimbatore,Saibaba Colony,-,-,Rs. 17470 - 20158
coimbatore,Saravanampatti,-,Rs. 9350 - 11050,Rs. 12772 - 13933
coimbatore,Singanallur,-,-,-
coimbatore,Thudiyalur,-,-,-
coimbatore,Uppilipalayam,-,-,Rs. 17680 - 19040
coimbatore,Vadavalli,-,Rs. 6800 - 8500,-
indore,AB Bypass Road,-,-,-
indore,AB Road Indore,-,-,Rs. 14608 - 16856
indore,Bengali Square,-,Rs. 9350 - 11900,Rs. 13430 - 17459
indore,Bicholi Mardana,-,Rs. 7896 - 10265,Rs. 14413 - 19217
indore,Dewas Naka(Panchvati),-,-,-
indore,Kanadia Road,-,-,-
indore,Khandwa Road,-,-,-
indore,Limbodi,-,-,-
indore,Mahalakshmi Nagar,-,Rs. 6885 - 8415,Rs. 8644 - 9605
indore,Manorama Ganj,-,-,Rs. 16198 - 18897
indore,Nipania,Rs. 10166 - 12708,Rs. 10453 - 12354,Rs. 15203 - 17967
indore,Niranjanpur,-,-,-
indore,Palasia,-,Rs. 11680 - 15274,Rs. 19768 - 24710
indore,Pipaliyahana,-,-,-
indore,Piplya Kumar,-,Rs. 9512 - 11414,Rs. 11092 - 12325
indore,Rajendra Nagar,-,-,-
indore,Rau,-,-,-
indore,Rau Road,-,-,-
indore,Saket Nagar,-,-,-
indore,Super Corridor,-,Rs. 7018 - 8772,-
indore,Vijay Nagar,-,Rs. 11220 - 14025,Rs. 16674 - 19240
nagpur,Ajni,-,Rs. 12266 - 14719,-
nagpur,Amravati Road,-,-,Rs. 14970 - 18178
nagpur,Bajaj Nagar,-,Rs. 11271 - 13005,-
nagpur,Beltarodi,-,-,-
nagpur,Besa,-,Rs. 6460 - 8075,-
nagpur,Bharat Nagar,-,Rs. 11169 - 12658,-
nagpur,Buti Bori,-,-,-
nagpur,Byramji Town,-,-,Rs. 14387 - 16600
nagpur,Civil Lines,-,Rs. 12390 - 14713,Rs. 21420 - 24990
nagpur,Clark Town,-,-,Rs. 21314 - 26329
nagpur,Dabha,-,-,-
nagpur,Dhantoli,-,Rs. 11067 - 13280,Rs. 17697 - 21236
nagpur,Dharampeth,-,Rs. 12368 - 14841,Rs. 21641 - 25058
nagpur,Dighori,-,Rs. 5454 - 6817,-
nagpur,Friends Colony,-,Rs. 7650 - 9945,Rs. 11725 - 13857
nagpur,Gandhi Nagar,-,Rs. 9180 - 10710,-
nagpur,Ganeshpeth Colony,-,Rs. 10542 - 13785,Rs. 20400 - 24225
nagpur,Godhani,-,-,-
nagpur,Godhani Road,-,Rs. 6215 - 6992,-
nagpur,Hazari Pahad,-,Rs. 8191 - 10424,-
nagpur,Hingna Road,-,Rs. 5692 - 7826,Rs. 9693 - 11846
nagpur,Hudakeshwar Road,-,-,-
nagpur,Jaiprakash Nagar,-,Rs. 12138 - 15606,-
nagpur,Jaitala Road,-,Rs. 6392 - 7990,-
nagpur,Katol Road,Rs. 5126 - 5638,Rs. 7650 - 9945,Rs. 11762 - 13901
nagpur,Khamla,-,Rs. 10542 - 12164,Rs. 16006 - 19435
nagpur,Khare Town,-,Rs. 11805 - 12543,-
nagpur,Koradi,-,Rs. 6215 - 6992,-
nagpur,Koradi Road,-,Rs. 6215 - 8546,-
nagpur,Laxminagar,-,Rs. 12278 - 14734,Rs. 20230 - 23800
nagpur,Mahal,-,-,-
nagpur,Manewada,-,-,-
nagpur,Manish Nagar,Rs. 5026 - 6143,Rs. 8500 - 9350,Rs. 11322 - 14719
nagpur,Mankapur,-,Rs. 6120 - 8415,-
nagpur,Medical Square,-,Rs. 13630 - 18173,Rs. 27616 - 34884
nagpur,Mihan,-,Rs. 7298 - 8109,-
nagpur,Mohan Nagar,-,Rs. 9591 - 11805,-
nagpur,Narendra Nagar,-,Rs. 7726 - 10044,Rs. 13005 - 15172
nagpur,New Colony,-,Rs. 13280 - 14756,-
nagpur,New Manish Nagar,-,Rs. 7635 - 9331,Rs. 11058 - 12164
nagpur,New Sneh Nagar,-,-,Rs. 15494 - 17707
nagpur,Nrendra Nagar Extension,-,Rs. 8415 - 9945,-
nagpur,Omkar Nagar,-,Rs. 7079 - 8848,-
nagpur,Pande Layout,-,-,Rs. 16600 - 17707
nagpur,Pratap Nagar,-,Rs. 11050 - 12750,Rs. 13719 - 17149
nagpur,Ramdas Peth,-,Rs. 13834 - 15678,Rs. 22416 - 25956
nagpur,Ram Nagar,-,Rs. 11353 - 15407,Rs. 17680 - 20995
nagpur,Rana Pratap Nagar,-,Rs. 11691 - 12590,-
nagpur,Ring Road,-,-,-
nagpur,Sadar,-,-,Rs. 16731 - 20317
nagpur,Seminari Hill,-,Rs. 8415 - 9945,Rs. 12658 - 14768
nagpur,Shankar Nagar,-,Rs. 12920 - 15342,-
nagpur,Shivaji Nagar,-,Rs. 11322 - 13586,Rs. 20187 - 23749
nagpur,Somalwada,-,Rs. 8330 - 10829,Rs. 12464 - 15863
nagpur,Subhash Nagar,-,Rs. 9313 - 11641,-
nagpur,Swawlambi Nagar,-,Rs. 11591 - 13375,Rs. 14015 - 16351
nagpur,Trimurti Nagar,Rs. 5848 - 7602,Rs. 9190 - 9956,Rs. 12872 - 16090
nagpur,Wanadongri,-,-,-
nagpur,Wardha Road,Rs. 4590 - 6120,-,-
nagpur,Wathoda,-,-,-
nagpur,Zingabai Takli,-,Rs. 6215 - 6992,-
vadodara,Ajwa Road,-,Rs. 5090 - 6786,-
vadodara,Akota,-,Rs. 11220 - 13090,-
vadodara,Alkapuri,-,-,-
vadodara,Atladra,-,Rs. 6120 - 7650,-
vadodara,Bhayli,-,Rs. 5902 - 8116,-
vadodara,Chhani,-,-,-
vadodara,Chhani Jakat Naka,-,-,-
vadodara,Diwalipura,-,Rs. 7650 - 8415,Rs. 11900 - 14280
vadodara,Elora Park,-,Rs. 8848 - 11503,Rs. 14025 - 16575
vadodara,Fatehgunj,-,Rs. 8920 - 11353,-
vadodara,Gorwa,-,Rs. 7956 - 9547,-
vadodara,Gotri,-,Rs. 7413 - 9060,Rs. 10503 - 14005
vadodara,Gotri Road,-,Rs. 8075 - 9690,Rs. 10503 - 12838
vadodara,Harni,-,-,Rs. 10625 - 11688
vadodara,Kalali,-,Rs. 5528 - 7107,-
vadodara,Kareli Bagh,-,-,Rs. 11900 - 15470
vadodara,Laxmipura,-,Rs. 8372 - 10884,Rs. 11092 - 13558
vadodara,Makarpura,-,-,-
vadodara,Manjalpur,-,Rs. 7512 - 10016,-
vadodara,New Alkapuri,-,Rs. 8372 - 10884,Rs. 11092 - 12325
vadodara,New Karelibaug,-,-,-
vadodara,New Sama,-,-,-
vadodara,New Sama Road,-,Rs. 7803 - 10404,Rs. 11432 - 13719
vadodara,Nizampura,-,Rs. 8109 - 9731,-
vadodara,Old Padra Road,Rs. 5100 - 5950,Rs. 9027 - 9930,Rs. 13600 - 17680
vadodara,Race Course Circle,-,-,-
vadodara,Sama,-,Rs. 8094 - 9892,Rs. 13252 - 15902
vadodara,Sama Savli Road,-,Rs. 7627 - 10169,-
vadodara,Sayajigunj,-,Rs. 9874 - 11669,-
vadodara,Sayajipura,-,-,-
vadodara,Sevasi,-,Rs. 8698 - 9664,-
vadodara,Soma Talav,-,-,-
vadodara,Subhanpura,-,Rs. 8882 - 10659,Rs. 13549 - 17614
vadodara,Sunpharma Road,-,Rs. 6732 - 7480,Rs. 11342 - 14178
vadodara,Tandalja,-,-,-
vadodara,Tarsali,-,-,-
vadodara,Vadsar,-,Rs. 5498 - 6283,-
vadodara,Vasant Vihar,-,-,Rs. 11276 - 12301
vadodara,Vasna-Bhayli-Road,-,Rs. 7222 - 8826,-
vadodara,Vasna Road,-,Rs. 7956 - 10343,Rs. 12750 - 14025
vadodara,Vemali,-,-,Rs. 9520 - 10710
vadodara,Waghodia,-,-,-
vadodara,Waghodia Road,-,-,-
chandigarh,Dera Bassi,-,-,Rs. 9369 - 10930
chandigarh,Kharar,-,-,-
chandigarh,Manimajra,-,-,-
chandigarh,Mohali,-,-,-
chandigarh,Mohalla Pharigat,-,-,-
chandigarh,Mullanpur,-,-,-
chandigarh,New Chandigarh,-,-,-
chandigarh,Sector-49B Chandigarh,-,-,Rs. 18253 - 20281
chandigarh,Sector 15-Chandigarh,Rs. 9960 - 13280,-,-
chandigarh,Sector 44-Chandigarh,-,-,-
chandigarh,Sector 45-Chandigarh,-,-,-
chandigarh,Sector 48-Chandigarh,-,-,Rs. 17707 - 21027
chandigarh,Sector 49-Chandigarh,-,Rs. 15640 - 20528,Rs. 21675 - 22950
chandigarh,Sector 50-Chandigarh,-,-,Rs. 18734 - 22678
chandigarh,Sector 51-Chandigarh,-,Rs. 16719 - 17702,-
chandigarh,Sector 63-Chandigarh,Rs. 10752 - 12708,Rs. 15895 - 18700,Rs. 19125 - 21675
chandigarh,Zirakpur,-,Rs. 9690 - 12597,Rs. 12041 - 14717
jaipur,Adarsh Nagar,-,-,-
jaipur,Ajmer Road,-,Rs. 6766 - 8458,Rs. 8582 - 10727
jaipur,Bani Park,-,-,Rs. 18774 - 21662
jaipur,Bapu Nagar,-,-,Rs. 21994 - 27859
jaipur,C-Scheme,-,Rs. 16040 - 20757,-
jaipur,Chitrakoot,-,Rs. 8224 - 10051,Rs. 12470 - 14963
jaipur,Civil Lines,-,-,Rs. 26316 - 32164
jaipur,Gandhi Path,-,-,Rs. 9585 - 11716
jaipur,Gopalpura Bypass,-,-,-
jaipur,Govindpura,-,-,-
jaipur,Jagatpura,-,Rs. 9350 - 11900,Rs. 10863 - 13277
jaipur,Malviya Nagar,-,Rs. 13260 - 15300,Rs. 16199 - 19938
jaipur,Mansarovar,-,-,Rs. 13090 - 15470
jaipur,Mansarovar Extension,-,Rs. 9602 - 11348,Rs. 12641 - 13790
jaipur,Narayan Vihar,-,-,-
jaipur,Nirman Nagar,Rs. 4781 - 5844,Rs. 9350 - 11220,Rs. 11237 - 13484
jaipur,Niwaru  Road,-,-,-
jaipur,Patrakar Colony,-,-,-
jaipur,Pratap Nagar,-,-,Rs. 8907 - 10180
jaipur,Raja Park,-,Rs. 11730 - 14662,Rs. 14790 - 17255
jaipur,Sanganer,-,-,Rs. 11954 - 11954
jaipur,Shyam Nagar,-,Rs. 8500 - 10200,Rs. 12325 - 14790
jaipur,Sikar Road,-,-,-
jaipur,Sirsi Road,-,Rs. 7358 - 9197,Rs. 9200 - 10350
jaipur,Sodala,Rs. 5311 - 6276,Rs. 7803 - 8670,-
jaipur,Swage Farm,-,Rs. 15606 - 18360,-
jaipur,Tilak Nagar,-,-,Rs. 27455 - 30345
jaipur,Vaishali Nagar,-,Rs. 9002 - 10802,Rs. 11908 - 15481
jaipur,Vidhyadhar Nagar,-,Rs. 8354 - 10210,Rs. 11067 - 14387
lucknow,Adil Nagar,-,-,-
lucknow,Amar Shaheed Path,-,Rs. 6885 - 8415,-
lucknow,Aziz Nagar,-,-,-
lucknow,Chinhat,-,Rs. 7512 - 9182,-
lucknow,Dewa Road,-,-,-
lucknow,Faizabad Road,-,Rs. 8361 - 9290,-
lucknow,Gomti Nagar,-,Rs. 11965 - 14956,Rs. 17713 - 21801
lucknow,Gomti Nagar Extension,-,-,-
lucknow,Hazrat Ganj,-,-,-
lucknow,IIM Road,-,-,-
lucknow,Indira Nagar,-,Rs. 8670 - 9392,Rs. 11949 - 14605
lucknow,Jankipuram,-,-,-
lucknow,Kanpur Road,-,-,-
lucknow,Kursi Road,-,-,-
lucknow,Lucknow Kanpur Highway,-,-,-
lucknow,Mahanagar,-,-,-
lucknow,New Hyderabad,-,-,Rs. 18785 - 21675
lucknow,Raebareli Road,-,Rs. 8882 - 9690,Rs. 11586 - 13903
lucknow,Sarojini Nagar,-,-,-
lucknow,Sitapur National Highway,-,-,-
lucknow,Sultanpur Road,-,-,-
lucknow,Sushant Golf City,-,Rs. 10200 - 10200,Rs. 13961 - 17064
lucknow,Uttardhauna,-,-,-
lucknow,Ved Nath Puram,-,-,-
lucknow,Vibhuti Khand,-,Rs. 14573 - 15545,Rs. 19635 - 22440
lucknow,Vrindavan Colony,-,-,Rs. 10565 - 11738
lucknow,Vrindavan Yojna,-,Rs. 7676 - 9211,Rs. 12478 - 13726
surat,Adajan,Rs. 5236 - 6807,Rs. 7971 - 9743,Rs. 10710 - 11900
surat,Althan,-,Rs. 10360 - 12243,Rs. 13192 - 14511
surat,Amroli,-,-,-
surat,Athwa,-,-,-
surat,Bhatar,-,Rs. 12912 - 14756,-
surat,Bhimrad,-,-,-
surat,Citylight Area,-,Rs. 14102 - 15042,Rs. 20012 - 23090
surat,Dindoli,-,-,-
surat,Dumas,-,-,-
surat,Dumas Road,-,-,-
surat,Ghod Dod Road,-,Rs. 13423 - 15341,-
surat,Jahangirabad,-,-,-
surat,Jahangirpura,-,-,-
surat,PAL,-,Rs. 7994 - 9771,Rs. 11858 - 15810
surat,Palanpur,-,Rs. 7130 - 7922,Rs. 9410 - 10455
surat,Palanpur Gam,-,Rs. 7079 - 7964,-
surat,Palanpur Jakatnaka,-,-,-
surat,Pal Gam,-,-,Rs. 13143 - 16063
surat,Parvat Patiya,-,-,-
surat,Piplod,-,Rs. 12912 - 13834,-
surat,Sachin,-,-,-
surat,Vankala,-,-,-
surat,Vesu,-,Rs. 11536 - 12498,Rs. 16269 - 17748
surat,VIP Road Vesu,-,-,Rs. 15317 - 18380
```