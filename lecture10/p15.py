'''
Pass a list in a lambda function and
return the sum of all the numbers in
the list (Hint: Use reduce functions of
functools library)
'''

from functools import reduce
my_list = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, my_list)
print("Sum of all numbers in the list:", total_sum)
