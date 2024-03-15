#Find Maximum of two numbers using Function

def find_maximum(num1, num2):
    return max(num1, num2)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

maximum = find_maximum(number1, number2)
print("Maximum of the two numbers is:", maximum)
