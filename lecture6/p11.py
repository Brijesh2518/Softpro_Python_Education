#WAP sentence as input, now count the occurence of word "The"
str = input("Enter the sentences: ")
#"The a spi people The hello go"
new_list = str.split()
count=0
for i in new_list:
    if ( i== "The"):
        count = count+1
    else:
        pass
print("total the sentences in string", count)