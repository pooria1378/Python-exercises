import requests
import json

api_key = "0414cd23db50db03cb2951ba525f3a8c"
base_url = "https://api.openweathermap.org/data/2.5/weather? "

city_name = input("Enter city name : ").title()

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

def kelvinToCelsius(kelvin):
    return int(kelvin - 273.15)

if x["cod"] != "404":

	y = x["main"]
	current_temperature = y["temp"]
	z = x["weather"]
	weather_description = z[0]["description"]



	print(str(city_name) + "`s temperature = " + str(current_temperature) + " Kelvin" + f" equals to: {kelvinToCelsius(current_temperature)} Celsius"+
          "\n Weather description = " + str(weather_description))

else:
	print(" City Not Found ")
