def calculate_farenheit(temperature_celcius) :
    """return temperature in farenheit if given temperature in celcius"""
    
    if temperature_celcius :
        temperature_celcius = float(temperature_celcius)
        temperature_farenheit = ((temperature_celcius) * 9 / 5) +32
        rounded_temperature_farenheit = round(temperature_farenheit, 1)
        
        return rounded_temperature_farenheit
    
def show_message(city, temperature_celcius) :
    """display message indicating current city and temperatures"""
    if city and temperature_celcius :
        print(f"It is currently {temperature_celcius}ºC ({temperature_farenheit}ºF) in {city}.")
    else: 
        print("Please enter a city and temperature")
    
city = input("What is the name of the city you are currently located in? ")
temperature_celcius = input("What is the temperature (in celcius) in your current location? ")
temperature_farenheit = calculate_farenheit(temperature_celcius)

calculate_farenheit(temperature_celcius)
show_message(city, temperature_celcius)

