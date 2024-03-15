#Using Lambda Function find the greatest between two numbers.

greater = lambda x, y: max(x, y)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
greatest = greater(num1, num2)
print("The greatest number is:", greatest)
