'''
Pass a list in a lambda function and
return the doubles of each number in
the list. (Hint: use map function)
'''


my_list = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, my_list))
print("Doubles of each number in the list:", doubled_numbers)
