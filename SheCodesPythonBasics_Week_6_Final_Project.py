from rich import print
import requests
from datetime import datetime


def show_current_weather(city): 
    """Shows details of current weather given a city input"""
        
    api_key = "dfc9t54e5b10fea0dcae14f3826ob4e6"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=imperial"

    response = requests.get(api_url)
    weather = response.json()
    temperature = round(weather["temperature"]["current"])
    city_name = weather["city"]
    country = weather["country"]
    
    print(f"The temperature in {city_name}, {country} is {temperature}ºF")

def show_forecast_weather(city):
    """Shows details of the future weather forecast given a city input"""
    api_key = "dfc9t54e5b10fea0dcae14f3826ob4e6"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}&units=imperial"

    response = requests.get(api_url)
    weather_forecast = response.json()
    #min_temperature = round(weather_forecast["daily"]["temperature"]["minimum"])
    #max_temperature = round(weather_forecast["daily"]["temperature"]["maximum"])
    city_name = weather_forecast["city"]
    country = weather_forecast["country"]
    
    for day in weather_forecast["daily"]:
       timestamp = day["time"]
       
       date = datetime.fromtimestamp(timestamp)
       formatted_day = date.strftime("%A")
       temperature = day["temperature"]["day"]
       print(f"{formatted_day}: {round(temperature)}ºF")
       
    
        #print(f"The weather forecast for {city_name}, {country} includes a low temperature of {min_temperature}ºF and a high temperature of {max_temperature}ºF)

city_name = input("Enter a city: ")
city_name = city_name.strip()
    
if city_name: 
    show_current_weather(city_name)
    show_forecast_weather(city_name)
else: 
    print("Please enter a city" )
