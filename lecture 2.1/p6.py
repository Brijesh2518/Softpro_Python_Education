#Temperature controler
c=int(input("Enter temperature in c:"))
f=int(input("Enter temperature in f:"))
c=f=(9*c)/5+32
f=c=(f-32)*5/9
print("temperature in c",f)
print("temperature in f",c)