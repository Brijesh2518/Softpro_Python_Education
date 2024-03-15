'''
Find minimum of two numbers using function
'''

def find_minimum(num1, num2):
    return min(num1, num2)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

minimum = find_minimum(number1, number2)
print("Minimum of the two numbers is:", minimum)
