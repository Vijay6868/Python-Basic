def BMI_Calculator(weight,height):
   "This calculates Body Mass Index (BMI)"
   BMI=weight/(height**2);
   return BMI

W=float(input("Enter weight in Kg ?"))
H=float(input("Enter  height in m  ?"))
YourBMI=BMI_Calculator(W,H);
print("Your BMI is:",YourBMI);
