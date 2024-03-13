#WAP to take the name of the user and print his short name
#Example:
#i/p Mahesh Kumar Singh
#0/p M.K.Singh
'''
name = input("Enter your full name: ")
parts = name.split()
short_name = ""
for i in range(len(parts)):
    if i == 0:
        short_name += parts[i][0].upper() + "."
    else:
        short_name += parts[i][0].upper()
print("Short name:", short_name)
'''

k = input("Enter your full name: ")
k2 = k.split()
k3 = k2 [0:len(k2)-1]
for i in k3:
    print(i[0],".",end="")
print(k2[-1])