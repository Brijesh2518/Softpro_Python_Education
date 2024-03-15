# WAP in python to find the value of cuboid using user defined function 

def valume(l,h,b):
    c = l*h*b
    return c 

a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))
c = int(input("Enter a 3rd number: "))

valume(a,b,c)
print(valume(a,b,c))