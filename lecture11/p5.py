# WAP to find the fibonacci series using recussive function 

def fibonacci(n):
    if n <= 0:
        return "Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(n):
    if n <= 0:
        print("Enter a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(1, n+1):
            print(fibonacci(i), end=" ")
a =int(input("Enter a number: "))
print_fibonacci_series(a)
