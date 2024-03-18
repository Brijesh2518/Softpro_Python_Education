# class Sum:
#     def usersum(self,c):
#         print("The sum is: ",c)
# Num1 = int(input("Enter First Num: "))
# Num2 = int(input("Enter First Num: "))
# c = Num1+Num2
# d = Sum()
# d.usersum(c)
#

# class add:
#     def sum(self,x,y):
#         s = x+ y
#         print("summation of the values =: ",s)
# a = add()
# b = add()
# a.sum(5,6)

class add:
    def sum(self,x,y):
        s = x+ y
        print("summation of the values =: ",s)
    def multi(self,x,y):
        m = x*y
        print("multi of the values =: ",m)
a = add()
a.sum(5,6)
a.multi(5,6)