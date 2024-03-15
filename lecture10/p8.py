# WAP to remove duplicates from string.

def remove_duplicates(input_string):
    unique_chars = set(input_string)
    result_string = ''.join(unique_chars)
    return result_string
input_string = input("Enter a string: ")
result = remove_duplicates(input_string)
print("String after removing duplicates:", result)
