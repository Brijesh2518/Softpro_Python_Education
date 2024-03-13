# input = "This_Is_A_Good_Morning"
#Output = tHIS.iS.a.gOOD.mORNING


str = "This_Is_A_Good_Morning"
new_str = ""

for i in str:
    if i.isupper():
        new_str = new_str+i.lower()
    elif i.islower():
        new_str = new_str + i.upper()
    elif i == "_":
        new_str = new_str + "."  
    else:
        new_str = new_str + i
print(new_str)        