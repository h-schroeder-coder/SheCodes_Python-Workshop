#SheCodesPythonHomework_Week_2

city_name = input("What is the name of the city you are currently in? ")
city_name = city_name.capitalize()
temperature_celcius = input("What is the current temperature in celcius? ")
temperature_celcius = float(temperature_celcius)

if len(city_name) > 2 and temperature_celcius > 20 :
    print(f"It is currently warm in {city_name} with a temperature of {temperature_celcius}ºC")
elif len(city_name) > 2 and temperature_celcius > 10 :
    print(f"It is currently chilly in {city_name} with a temperature of {temperature_celcius}ºC")
elif len(city_name) > 2 and temperature_celcius < 10 :
    print(f"It is currently cold in {city_name} with a temperature of {temperature_celcius}ºC")
else:
    print("Please try again and enter a city and temperature")    