class Employee:
    def details(self,empid,empname,empsalary):
        self.empid = empid
        self.empname = empname
        self.empsalary = empsalary
    def display(self):
        print("employee id: ",self.empid)
        print("employee name: ",self.empname)
        print("employee empsalary: ",self.empsalary)

e = Employee()
eid = int(input("Enter the Id: "))
ename = input("Enter the Name: ")
esalary = int(input("Enter the salary: "))
e.details(eid,ename,esalary)
e.display()