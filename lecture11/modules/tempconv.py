# WAP a python program to create a module named tempconv. in tempconv module create to function ctof() and ftoc(). ctof() function converts temperature from centigrade to fahrenheit and ftoc() function converts temperature from fahrenehit to centigrade. Now import tempconv module and test ctof() and ftoc() function.
def ctof(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def ftoc(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
