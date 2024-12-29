# SheCodesPythonHomework_Week_1

name = input("What is your name? ")
city = input("What city do you live in? ")
temperature = input("What is the current temperature in celcius? ")
temperature_c = float(temperature)
temperature_f = temperature_c * 9/5 + 32
rounded_temperature_f = round(temperature_f, 1)
print(f"Hi {name.capitalize()}, you are in {city.capitalize()}, and it is currently {temperature_c}ºC or {rounded_temperature_f} ºF.")

low_temperature_c = temperature_c - 10
low_temperature_f = (low_temperature_c * 9/5) + 32
rounded_low_temperature_f = round(low_temperature_f, 1)
print(f"I predict that tonight, the temperature will reach {low_temperature_c}ºC or {rounded_low_temperature_f}ºF.")

print("Have a good day!")