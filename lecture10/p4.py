'''
Take two integers input from the user
and swap the values using functions.
'''

def swap_integers():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2
result1, result2 = swap_integers()
print("After swapping:")
print("First integer:", result1)
print("Second integer:", result2)
