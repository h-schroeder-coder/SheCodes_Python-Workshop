from rich import print
import requests

city = input("Enter a city name ")

api_key = "dfc9t54e5b10fea0dcae14f3826ob4e6"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=imperial"

response = requests.get(api_url)
weather = response.json()
temperature = round(weather["temperature"]["current"])
city = weather["city"]
country = weather["country"]

print(f"It is currently {temperature}ºF in {city}, {country}")