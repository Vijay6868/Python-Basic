def FileDecryptor2(FileName):
       "This function decrypt an encrypted file"
       FO1 = open(FileName,'r')
       DATA = ""
       for line in FO1:
              code = int(line.strip())
              DATA = DATA + chr(int((code-5)/6))
       FO2 = open("NewFile2.txt",'w')
       FO2.write(DATA)
       FO1.close()
       FO2.close()
       return

FileDecryptor2("en2_names.txt")

