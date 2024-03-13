#Compress String 

#str = "aaaabbbccccddkmmmmm"        Requiredment 
#new_str = "a4b3c4d2k1m5"
'''
user=input("Enter a str: ")
blanck_string=""
for i in user:
    if i in blanck_string:
        pass
    else:
'''





'''
user=input("Enter a str: ")
compressed = "" 
count = 1 
for i in user(1, len(user)):
    if compressed[i] == user[i - 1]:
        count += 1
    else:
        compressed += user[i - 1] + str(count)
        count = 1
compressed += user[-1] + str(count)
print("Compressed string:", compressed)
'''      



'''
str = "aaaabbbccccddkmmmmm"
compressed = "" 
count = 1 
for i in range(1, len(str)):
    if str[i] == str[i - 1]:
        count += 1
    else:
        compressed += str[i - 1] + str(count)
        count = 1
compressed += str[-1] + str(count)
print("Compressed string:", compressed)
'''



str_inp = "aaaabbbccccddkmmmmm"
blanck_str = ""
for i in str_inp:
    count = 1
    if str_inp[i] == str_inp[i - 1]:
          count += 1
    else:
        blanck_str += str_inp[i-1] + str_inp(count)
        count+1
        blanck_str += str[-1] + str(count)
print("Compressed Number", blanck_str)
        


        
    