## lesson 2

# Import datetime
#from datetime import datetime

# Display the current date and time (no formatting)
#now = datetime.now()
#print(now)

# Display the current date and time following this format: Date: Jan 12, 2032 Time: 14:03
#formatted_date = now.strftime("Date: %b %d, %Y Time: %H:%M")
#print(formatted_date)

# Convert this time stamp 1705590204 into a date and display only the time using this format: 2:30am
#from datetime import datetime
#timestamp = 1705590204
#date = datetime
#date_from_timestamp = date.fromtimestampt(timestamp)
#print(date_from_timestamp)


# lesson 3
# Install rich
from rich import print
# Print your name in Red
print("[red]Hannah Schroeder[/red]")
# Bonus point: Print your name in red, bold and underlined
print("[red underline bold]Hannah Schroeder[/red underline bold]")


# lesson 4
# Install and import 'requests'
import requests

# Get and print out the response from this URL 
#https://jsonplaceholder.typicode.com/photos/1

response = requests.get("https://jsonplaceholder.typicode.com/photos/1")
print(response)

# Print out the title and thumbnail url of the photo from the response
photo = response.json()
print(photo["title"])
print(photo["thumbnailUrl"])


# lesson 5

#Create a Repl
#done
#Display the current weather humidity in Tokyo, such as:
#It is currently 10ºC in Tokyo, Japan and the humidity level is 40%

city = "Tokyo"
api_key = "dfc9t54e5b10fea0dcae14f3826ob4e6"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=imperial"

response = requests.get(api_url)
weather = response.json()
temperature = round(weather["temperature"]["current"])
country = weather["country"]
humidity = weather["temperature"]["humidity"]

print(f"It is currently {temperature}ºF in {city}, {country} and the humidity level is {humidity}%")