# lesson 2
#def current_weather(): 
#    current_city = input("What is the city you are currently in? ")
#    current_temperature = input("What is the current temperature in celcius? ")
#    if current_city and current_temperature : 
#        print(f"You are in {current_city.capitalize()} and it is currently {current_temperature}ºC.")
#    else:
#        print("Please enter a city and temperature")
        
#current_weather()
#current_weather()


# lesson 3
#def display_current_weather(current_city, current_temperature):
#    """Request current location and weather details"""
#    if current_city and current_temperature : 
#        print(f"The temperature in {current_city.capitalize()} is currently {current_temperature}ºC.")
    
#current_city = input("What is the city you are currently in? ")
#current_temperature = input("What is the current temperature in celcius? ")    

#display_current_weather(current_city, current_temperature)
#display_current_weather("Fall Creek", "1")
#display_current_weather("Wichita", "5")

# lesson 4
#def display_current_weather(current_city, current_temperature, current_humidity=""):
#    """Request current location and weather details"""
#    if current_city and current_temperature and current_humidity : 
#        print(f"The temperature in {current_city.capitalize()} is {current_temperature}ºC. with a humidity of {current_humidity}%")
#    elif current_city and current_temperature : 
#        print(f"The temperature in {current_city} is {current_temperature}ºC.")
#    else:
#        print("Please provide a city and temperature")
#    
#current_city = input("What is the city you are currently in? ")
#current_temperature = input("What is the current temperature in celcius? ")
#current_humidity = input("What is the current percent humidity? ")    

#display_current_weather(current_city, current_temperature, current_humidity)
#display_current_weather("Fall Creek", "1", "65")
#display_current_weather("Wichita", "5", "")

# lesson 5
def calculate_farenheit (temperature_celcius) :
  """Return the Farenheit value of a celcius temperature"""
  temperature_farenheit = (float(temperature_celcius) * 9 / 5) +32
  
  return temperature_farenheit

temperature_celcius = 15

temperature_farenheit = calculate_farenheit(temperature_celcius)
city = "London"

print(f"It is currently {temperature_celcius}ºC ({temperature_farenheit}ºF) in {city}")