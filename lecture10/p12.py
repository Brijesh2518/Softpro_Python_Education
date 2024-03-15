# Swap the variables using the lambda function 
num1 = 5
num2 = 10
print("Before swap: num1 =", num1, "num2 =", num2)
num1, num2 = map(lambda x: num2 if x == num1 else num1, (num1, num2))
print("After swap: num1 =", num1, "num2 =", num2)
