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
def display_current_weather(current_city, current_temperature):
    """Request current location and weather details"""
    if current_city and current_temperature : 
        print(f"The temperature in {current_city.capitalize()} is currently {current_temperature}ºC.")
    
current_city = input("What is the city you are currently in? ")
current_temperature = input("What is the current temperature in celcius? ")    

display_current_weather(current_city, current_temperature)
display_current_weather("Fall Creek", "1")
display_current_weather("Wichita", "5")