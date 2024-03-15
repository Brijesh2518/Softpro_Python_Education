# num2 =["rahul","mukesh","ranveer"]
# count the number of string starting with "r" 

num2 = ["rahul", "mukesh", "ranveer"]
count = 0

for string in num2:
    if string.startswith("r"):
        count += 1
print("Number of strings starting with 'r':", count)
