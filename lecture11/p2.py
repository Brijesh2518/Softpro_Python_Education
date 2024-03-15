# WAP to find the factorial using normla function 

def fact(n):
    mul = 1
    for i in range(1,n+1):
        mul = mul*i
    return mul
a = int(input("Enter a number: "))
print("Factorial is =",fact(a))