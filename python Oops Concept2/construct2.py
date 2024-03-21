class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def rectarea(self):
        return self.length * self.breadth
    def rectperi(self):
        return 2*(self.length + self.breadth)

l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breathe of the rectangle: "))
obj1 = rectangle(l,b)
ar = obj1.rectarea()
print("Area of the rectangle is =",ar)
pr = obj1.rectperi()
print("Perimeter of the rectangle is =",pr)