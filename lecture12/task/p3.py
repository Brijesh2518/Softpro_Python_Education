# 3. compress the string 
# str = "aaaabbbccd"
# Define the input string
s = (input("Enter a string: "))
compressed_str = ""
count = 1
for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        compressed_str += s[i] + str(count)
        count = 1
print("Compressed string:", compressed_str)
