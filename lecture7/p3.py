input=input("Enter a str: ")
new_str = ""
for i in input:
    count=0
    if i not in new_str:
        for j in input:
            if(i==j):
                count=count+1
    if(count!=0):
                new_str=new_str+i+str(count)
print("COmpressed Number",new_str)

    
    