# To check weather a number is prime or not 

n = int(input("Enter a number: "))
for i in range(2,15):
    if(n%i==0):
        print("Number is not prime number")
        break
else:
    print("Number is prime number")