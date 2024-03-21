#Two objects of the same class,passig data of multiple users
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu   
        self.ram=ram
    def display(self):
        print("details=",self.cpu,self.ram)
comp1=computer('i5',16)
comp2=computer('i7',32)

comp1.display()
comp2.display()
    