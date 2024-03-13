# WAP to get the the reverse of digits of a number

num=int(input("Enter a digits: "))
sum=0
while(num>0):
    dig = num % 10
    sum = (sum * 10) + dig
    num //= 10
print("Value of digits",sum)