import tempconv
celsius_temp=int(input("Enter a celsius number: "))
fahrenheit_result = tempconv.ctof(celsius_temp)
print(f'{celsius_temp} Celsius = {fahrenheit_result} Fahrenheit')
fahrenheit_temp=int(input("Enter a fahrenheit number: "))
celsius_result = tempconv.ftoc(fahrenheit_temp)
print(f'{fahrenheit_temp} Fahrenheit = {celsius_result} Celsius')
