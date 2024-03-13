#WAP to take string from user and check weather it is a reverse
a=input("Enter a str: ")
a1=a[::-1]
reversed(a)
if (a1==a):
    print("Palindrome")
else:
    print("Not Palindrome")

