# Valid Parenthesis 

s = input("Enter a string with parentheses: ")
balance = 0

for char in s:
    if char == '(':
        balance += 1
    elif char == ')':
        balance -= 1

if balance == 0:
    print("The string contains valid parentheses.")
else:
    print("The string does not contain valid parentheses.")
