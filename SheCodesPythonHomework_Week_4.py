# Exercise 1
weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}

def round_temps_c (temperature_celcius):
    temperature_celcius = weather["temperature"]
    return round({temperature_celcius})

def round_temps_f (temperature_celcius):
    temperature_celcius = weather["temperature"]
    temperature_farenheit = ({temperature_celcius} * 9 / 5) +32
    return round({temperature_farenheit})

round_temps_c(temperature_celcius)
round_temps_f(temperature_celcius)

print(f"{round_temps_c(weather["temperature"])}ºC ({round_temps_f(weather["temperature"])}ºF) in {weather["city"]}, {weather["country"]}, the humidity level is {weather["humidity"]}%.")



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

print(forecast["daily"])