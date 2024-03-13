#find the average of list


my_list = [4,8,0,5,3]
sum = 0
for number in my_list:
    sum += number
count = len(my_list)
average = sum / count
print(f"The average of the list is {average:.1f}.")
