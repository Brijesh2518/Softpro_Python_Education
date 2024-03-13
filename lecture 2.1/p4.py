# Electricity bill generator
a = int(input("Enter unit range:"))
if(a<=150):
          bill =3*a
          print("balance",bill)
elif(a>150 and a<=300):
        bill = 4*a
        print("balance",bill)
else:
        bill=5*a
        print("balance",bill)