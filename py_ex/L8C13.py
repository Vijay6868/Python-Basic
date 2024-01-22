def encryptor(string):
       "This function encrypt a string by using ASCII codes"
       out=[]
       for letter in string:
              code = ord(letter)
              out = out + [code]
       return out 

def FileEncryptor(OriginalFile):
       "This function encrypt a file by using ASCII codes"
       EncryptedFile = "En_"+OriginalFile
       FO1 = open(OriginalFile,'r')          
       FO2 = open(EncryptedFile,'w')            
       DATA1 = FO1.read()
       Codes = encryptor(DATA1)
       for code in Codes:
              FO2.write(str(code)+"\n")
       FO1.close()
       FO2.close()
       return

FileEncryptor("names.txt")
       




       
