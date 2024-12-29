def current_weather(): 
    current_city = input("What is the city you are currently in? ")
    current_temperature = input("What is the current temperature in celcius? ")
    if current_city and current_temperature : 
        print(f"You are in {current_city.capitalize()} and it is currently {current_temperature}ºC.")
    else:
        print("Please enter a city and temperature")
        
current_weather()
current_weather()
