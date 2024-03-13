# simple def funtion 

def update(ls):
    print(id(ls))
    ls[1] = 25
    print("ls",ls)
    
    
lst = [10,20,30]
print(id(lst))
update(lst)
print("lst",lst)