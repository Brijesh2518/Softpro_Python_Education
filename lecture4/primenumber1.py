# WAP to check the given number is prime number or not (range n1,n2)

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
for i in range(n1,n2):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)