# wap to create a class with 'student' in this class
# take Rollno ,name and fee now create a method display.

class student:
    def details(self,rollno,name,fee):
        self.rollno = rollno
        self.name = name
        self.fee = fee
    def display(self):
        print("Student Roll no: ",self.rollno)
        print("Student Name: ",self.name)
        print("Student fee: ",self.fee)

acd = student()
Stu_Rollno = int(input("Student Roll no: "))
Stu_Name = input("Student Name: ")
Stu_fee = int(input("Student fee amount: "))
acd.details(Stu_Rollno,Stu_Name,Stu_fee)
acd.display()
