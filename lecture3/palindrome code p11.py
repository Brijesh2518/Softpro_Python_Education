num=1218
temp =num
rev=0
while(temp>0):
    dig=temp%10
    rev=(rev*10)+dig
    temp=temp//10
if(temp==rev):
    print("the number of palindrome",rev)
else:
    print("The given is not palindrome",rev)