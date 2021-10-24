#!/usr/local/bin/python3

import json
import requests
import os

# Get a Zillow listing in a specific city
def city_search(city):
    # Grab JSON from Zillow API and parse JSON response
    params_list = {'access_token': os.environ['ZILLOW_KEY'], 'near': city, 'zestimate.lte': 164000, 'limit': "1"}
    response = requests.get("https://api.bridgedataoutput.com/api/v2/zestimates_v2/zestimates", params=params_list)
    parsed_json = json.loads(response.text)
    
    # Grab zillow URL, zestimate and address
    zillow_url = parsed_json['bundle'][0]['zillowUrl']
    zestimate = parsed_json['bundle'][0]['zestimate']
    address = parsed_json['bundle'][0]['address']

    return (address, zillow_url, zestimate)