import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()
pp = PrettyPrinter()
from dotenv import load_dotenv
import os
load_dotenv()
import json

api_key = os.getenv('api_key')

def fetchAsteroidNeowsLookup():
	asteroid_id = '3542519'
	URL_NeoLookup = "https://api.nasa.gov/neo/rest/v1/neo/"+ asteroid_id
	params = {
			'api_key':api_key
	}
	response = requests.get(URL_NeoLookup,params=params).json()
	json.dump(response, open('anl.json', 'w'), indent=4)
	
fetchAsteroidNeowsLookup()
