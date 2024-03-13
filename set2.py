# Take a list as an input from user and remove all its duplicates using set().
'''
user_input = input("Enter elements of the list: ")
input_list = user_input.split()
input_list = list(set(input_list))
print("List after removing duplicates:", input_list)
'''

'''
def remove_duplicates(input_list):
    unique_elements = set(input_list)
    result_list = list(unique_elements)
    return result_list
user_input = input("Enter elements of the list : ")
input_list = user_input.split()
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)
'''

input_list= input("Enter elemets of the list: ")
unique_set = set(input_list)
unique_list= list(unique_set)
print("List with duplicates removed", unique_list)