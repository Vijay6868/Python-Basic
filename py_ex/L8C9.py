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

FO1=open("data.txt",'r')
FO2=open("out.txt",'w')
N = 5
for c in range(1,N+1):
       name = FO1.readline()
       name=name.strip()
       W = int(FO1.readline())
       H = float(FO1.readline())
       BMI = BMI_Calculator(W,H)
       BMI = round(BMI,2)
       Class = BMI_Class(BMI)
       result = name + " " + str(BMI) + " "  + Class + "\n"
       FO2.write(result)
FO1.close()
FO2.close()
       

