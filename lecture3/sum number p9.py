#write a program to get the sum of digits of numbers 

num=int(input("Enter a digit: "))
sum=0
while(num >0):
    dig = num % 10
    sum = sum + dig
    num = num //10
print("Value of digits",sum)