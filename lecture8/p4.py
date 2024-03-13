# Using the keyword in python
new_list = [4,5,7,5,8,9,10,4]
new_list.sort()
print(new_list)
print(len(new_list))
    
#without using keyword in python

my_list = [64, 34, 25, 12, 22, 11, 90]
n = len(my_list)
for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print("Sorted list:", my_list)
