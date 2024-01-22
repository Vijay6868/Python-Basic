def BMI_Calculator(weight,height):
   "This calculates Body Mass Index (BMI)"
   BMI=weight/(height**2);
   return BMI

def BMI_Class(BMI):
    "This function find your BMI class"
    if BMI>=40:
        Class="Obesity Class III"
    elif BMI>=35:
        Class="Obesity Class II"
    elif BMI>=30:
        Class="Obesity Class I"
    elif BMI>=25:
        Class="Over Weight"
    else:
        Class="Normal"
    return Class

W=float(input("Enter weight in Kg ?"))
H=float(input("Enter  height in m  ?"))
YourBMI=BMI_Calculator(W,H)
Class=BMI_Class(YourBMI)
print("Your BMI class is:",Class)








