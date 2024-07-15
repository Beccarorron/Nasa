import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()
pp = PrettyPrinter()
from dotenv import load_dotenv
import os
import json
load_dotenv()

api_key = os.getenv('api_key')

URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"  # Define the variable URL_NeoFeed and assign it a value

params = {
	'api_key':api_key,
	'start_date':'2024-05-25',
	'end_date':'2024-06-01'
}

response = requests.get(URL_NeoFeed,params=params).json()
json.dump(response, open('adn.json', 'w'), indent=4)

