# WAP to print fibonacci series using basic funtion 

def fib(x):
    a=0
    b=1
    print(0,end="")
    print(1,end="")
    for i in range(x):
       sum=a+b
    print(sum,end="")
    a=b
    b=sum
nums=int(input("Enter a number: "))
fib(nums)

