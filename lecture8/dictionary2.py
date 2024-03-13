#WAP to take input name and % of marks of students in a dictionary and disply the information.

dic1={}
n=int(input("Enter number of students: "))
i=1
while i<=n:
    name=input("Enter Student Name: ")
    marks=input("Enter % of marks of student: ")
    dic1[name]=marks
    i=i+1
for x in rec:
    print(x,dic1[x])