'''
Write a function to swap the values
of first and last position in a list.
 Example: if list =[1,2,3,4,5] then output
 should be
'''

def swap_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
my_list = [1, 2, 3, 4, 5]
result_list = swap_first_last(my_list)
print(result_list) 
