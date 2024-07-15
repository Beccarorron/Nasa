import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()
pp = PrettyPrinter()
from dotenv import load_dotenv
import os
load_dotenv ()
import json

api_key = os.getenv('api_key')

def fetchEPICData():
	URL_EPIC = "https://api.nasa.gov/EPIC/api/natural/2024-05-31/jpg/epic_1b_20240531011359.jpg"
	params = {
		'api_key':api_key,
	}
	response = requests.get(URL_EPIC,params=params).raw

	pp.pprint(response)
fetchEPICData()