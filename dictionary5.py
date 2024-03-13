#WAP to check the number of occurrence of each character present in a string.

str = "aabcdaab"
#output = {'a':4,'b':2,'c':1,'d':1}

word = input("Enter any word: ")
d = {}
for i in word:
    d[i] = d.get(i,0) + 1
for k,v in d.items():
    print(k,"Occured",v,"times")