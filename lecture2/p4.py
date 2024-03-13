import math
a = float(input("Enter a first num: "))
b = float(input("Enter a second num: "))
c = float(input("Enter a third num: "))
d=(b*b)-(4*a*c)
if(d<0):
    print("Roots are imaginary")
else:
    
    root1=(-b+ math.sqrt(d))/2*a
    root2=(-b- math.sqrt(d))/2*a

#rootacs1 = -b + sqrt(b**2-4*a*c)/2*a
#rootacs1 = -b - sqrt(b**2-4*a*c)/2*a