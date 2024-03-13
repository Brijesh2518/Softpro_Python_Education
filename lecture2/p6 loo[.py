'''for loop
range (Starting point,end point,diff)
range(5)
0,1,2,3,4for i in range(3):
    #for j in range(j=i+1):
    print("*")'''
    
#print("hello")
#print("world")

for i in range(3):
    for j in range(i+1):
        print("*",end="")
    print()
