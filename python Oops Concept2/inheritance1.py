class A:
    def feature1(self):
        print("You are inside the class A and feature1 ")
    def feature2(self):
        print("You are inside the class A and feature2 ")
class B(A):
    def feature3(self):
        print("You are inside the class B and feature3 ")
    def feature4(self):

        print("You are inside the class B and feature4 ")
a = A()
a.feature1()
a.feature2() 
b = B()
b.feature1()
b.feature3()