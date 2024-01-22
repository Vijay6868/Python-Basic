def HowManyRecords(FileName):
   "Find the number of lines in FileName.txt"
   FO=open(FileName,'r')
   L = 0
   for line in FO:
      L = L + 1
   N = L/3
   return int(N)

print(HowManyRecords("data.txt"))


   

       

