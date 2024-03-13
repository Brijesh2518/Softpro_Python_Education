# Remove duplicate from a string 

#str = "aabcdaakm"
#new_str="abcdkm


user=input("Enter a Str: ")
black_string= ""
for i in user:
    if i in black_string:
        pass
    else:
        black_string=black_string+i
print("String Duplicate",black_string)
