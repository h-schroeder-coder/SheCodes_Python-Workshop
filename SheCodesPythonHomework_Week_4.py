# Exercise 1

def convert_temps_f (temperature_celcius):
    temperature_farenheit = (temperature_celcius * 9 / 5) +32
    return temperature_farenheit


weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}

city = weather["city"]
country = weather["country"]
temperature = weather["temperature"]
humidity = weather["humidity"]
temperature_farenheit = convert_temps_f(temperature)


print(f"It is {round(temperature)}ºC ({round(temperature_farenheit)}ºF) in {city}, {country}, the humidity level is {humidity}%.")



# Display the weather in Lisbon such as:
# It is 18ºC (64ºF) in Lisbon, Portugal, the humidity level is 77%.


# Exercise 2
forecast = {
  "city":"Lisbon",
  "country":"Portugal",
  "daily":
    [
      17.76,
      13.08,
      12.14,
      11.25,
      14.29
    ]
}

# Display the forecast in Lisbon such as:
# The forecast for Lisbon, Portugal for the next 5 days is:
# Day 1: 18ºC
# Day 2: 13ºC
# Day 3: 12ºC
# Day 4: 11ºC
# Day 5: 14ºC

city = forecast["city"]
country = forecast["country"]

print(f" The forecast {city}, {country} for the next 5 days is:")

index = 0
for temperature in forecast["daily"]:
    temperature_farenheit = round(convert_temps_f(temperature))
    print(f"Day {index +1}: {round(temperature)}ºC ({round(temperature_farenheit)}ºF)")
    index = index + 1