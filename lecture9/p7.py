# WAP too make a simple calculator user defined functions.

def cal(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d
s = int(input("Enter a 1st number: "))
m = int(input("Enter a 2nd number: "))
a,b,c,d =cal(s,m)
print("Addition of a: ",a)
print("Substraction of a: ",b)
print("Multiplication of a: ",c)
print("Division of a: ",d)
