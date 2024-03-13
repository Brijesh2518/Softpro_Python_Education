#WAP to take the name of the user and print his short name

c = 0
s=input("Enter a name: ")
s1=s.split()
for i in s1:
    if i=="the":
        c=c+1
print(c)