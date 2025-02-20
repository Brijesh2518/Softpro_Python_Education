# Check the Anagram String or not ....
'''
def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2
input_str = "SILENT"
compare_str = "LISTEN"
result = is_anagram(input_str, compare_str)
print(result)
'''

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

s =input("Enter a string: ")
output_str=input("Enter Outpiut String: ")
if is_anagram(s, output_str):
    print(f"{output_str} is an anagram of {s}")
else:
    print(f"{output_str} is not an anagram of {s}")

