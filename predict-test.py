#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'


customer = {"Gender": 2.0,
 "Age": 35.0,
 "Driving_License": 1.0,
 "Region_Code": 47.0,
 "Previously_Insured": 1.0,
 "Vehicle_Age": 1.0,
 "Vehicle_Damage": 1.0,
 "Annual_Premium": 15000.0,
 "Policy_Sales_Channel": 151.0,
 "Vintage": 148.0}


response = requests.post(url, json=customer).json()
print(response)

if response['Insurance'] == False:
    print('sending promo email to customer')
else:
    print('not sending promo email to customer')