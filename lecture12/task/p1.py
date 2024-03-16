'''
Question -1
	    *
       * *
      * * *
     * * * *

'''
'''
for i in range(5):
    for j in range(i):
       print("*",end=" ")
    print()
'''   


for i in range(5):
    print(" " * (5 - i - 1), end="")
    print("* " * (i + 1))
