class Sum:
    def usersum(self,c):
        print("The sum is: ",c)
    def sub1(self,sub):
        print("The subtration is: ",sub)
    def multi1(self,multi):
        print("The multipication is: ", multi)

Num1 = int(input("Enter First Num: "))
Num2 = int(input("Enter Second Num: "))
c = Num1+Num2
sub = Num1-Num2
multi = Num1*Num2
d = Sum()
d.usersum(c)
d.sub1(sub)
d.multi1(multi)