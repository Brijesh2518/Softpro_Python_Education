# Take a tupple input from user and call its sum and avg.
#new_tupple = (10,20,30)
new_tupple = eval(input("Enter a tupple: "))
ln = len(new_tupple)
sum = 0
for i in new_tupple:
    sum = sum +i
print("Summation of tupple is ",sum)
print("Avg of tupple is ",sum/ln)
