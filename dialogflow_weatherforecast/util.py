from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

headers = {
	'Accepts': 'application/json',
	'APIKEY': '4f924ca39577558056e0e7087dc229f8',
}

session = Session()

def getWeather(countryname):
	countryname = countryname.lower()
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(countryname, headers['APIKEY'])
	
	response = session.get(url)
	data = json.loads(response.text)
	weather = data["weather"][0]["description"]
	return weather
	