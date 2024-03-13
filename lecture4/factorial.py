# WAP to print factorial series

n = int(input("Enter the number: "))
mul = 1
for i in range(1,n+1):
    mul = mul * i
print("Factorial is: ",mul)
