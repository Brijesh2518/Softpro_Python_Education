'''
Pass a list in a lambda function and
return only the positive numbers in the
list. (Hint: Use the filter function)

'''

my_list = [-1, 2, -3, 4, -5, 6]
positive_numbers = list(filter(lambda x: x > 0, my_list))
print("Positive numbers in the list:", positive_numbers)
