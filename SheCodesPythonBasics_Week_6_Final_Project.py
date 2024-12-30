from rich import print
import requests
from datetime import datetime

def show_temp(day, temperature, unit='F') :
    """Shows temperatures with a day"""
    print(f"[blue]{day}[/blue]: {round(temperature)}º{unit}")

def show_current_weather(city): 
    """Shows details of current weather given a city input"""
        
    api_key = "dfc9t54e5b10fea0dcae14f3826ob4e6"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=imperial"

    response = requests.get(api_url)
    weather = response.json()
    temperature = round(weather["temperature"]["current"])
    city_name = weather["city"]
    country = weather["country"]
    
    print(f"[blue]Currently,[/blue] the temperature in {city_name}, {country} is {temperature}ºF")
    
def show_forecast_weather(city):
    """Shows details of the future weather forecast given a city input"""
    api_key = "dfc9t54e5b10fea0dcae14f3826ob4e6"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}&units=imperial"

    response = requests.get(api_url)
    weather_forecast = response.json()
    print("\n[cyan bold]Forecast: [/cyan bold]")
    
    for day in weather_forecast["daily"]:
       timestamp = day["time"]
       
       date = datetime.fromtimestamp(timestamp)
       formatted_day = date.strftime("%A")
       temperature = day["temperature"]["day"]
       
       if date.date() != datetime.today().date() :
           show_temp(formatted_day, round(temperature))

def show_welcome():
    """Shows welcome message"""
    print("[cyan bold]Welcome to my weather app[/cyan bold]")

def show_credit():
    """Shows credit message"""
    print("\n[green] This app was built by Hannah Schroeder[/green]")

show_welcome()
city_name = input("Enter a city: ")
city_name = city_name.strip()
    
if city_name: 
    show_current_weather(city_name)
    show_forecast_weather(city_name)
    show_credit()
else: 
    print("Please enter a city" )
