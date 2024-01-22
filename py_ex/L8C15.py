def decryptor(Codes):
       "This function convert a list of ASCII codes to a string"
       out = ""
       for code in Codes:
              out = out + chr(code)
       return out 

def FileDecryptor(FileName):
       "This function decrypt a file by using ASCII codes"
       FO1 = open(FileName,'r')
       DATA = ""
       for line in FO1:
              code = int(line.strip())
              DATA = DATA + chr(code)
       FO2 = open("NewFile.txt",'w')
       FO2.write(DATA)
       FO1.close()
       FO2.close()
       return

FileDecryptor("en_names.txt")



       
