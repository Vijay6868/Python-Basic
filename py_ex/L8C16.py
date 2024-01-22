def encryptor2(string):
       "This function encrypt a string by using ASCII codes"
       out=[]
       for letter in string:
              x = ord(letter)
              y = 6*x + 5
              out = out + [y]
       return out 

#def FileEncryptor2(OriginalFile):
       "This function encrypt a file by using ASCII codes"
       EncryptedFile = "En2_"+OriginalFile
       FO1 = open(OriginalFile,'r')          
       FO2 = open(EncryptedFile,'w')            
       DATA1 = FO1.read()
       #Codes = encryptor2(DATA1)
       #for code in Codes:
              #FO2.write(str(code)+"\n")
       #FO1.close()
       FO2.close()
       return

print(encryptor2("iman"))
       




       
