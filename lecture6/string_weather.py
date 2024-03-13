#WAP to take string from user and check weather it is a Palindrome or not 
a=input("Enter a str: ")
a1=a[::-1]
if (a1==a):
    print("Palindrome")
else:
    print("Not Palindrome")

