import requests

def weather_info(city,units):
	if units=='imperial' or 'metric':
		base=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid=0e9b3da6d347073f65a25f7c4be4104f'
	else:
		base=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0e9b3da6d347073f65a25f7c4be4104f'

	return requests.get(base).json()

#print(weather_info('bangalore','metric'))