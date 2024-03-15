# WAP to find the factorial using recusrsion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input("Enter a number to find factorial: "))
print("Factorial =",fact(x))
    