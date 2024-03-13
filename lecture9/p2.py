# call by value and call by references
def update(lst):
    for i in lst:
        i = i+1
        lst.insert(0,i)
    print(lst)
    
list = [1,2,3,4]
update(list)
print(list)