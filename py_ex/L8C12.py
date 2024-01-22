def encryptor(string):
       "This function encrypt a string by using ASCII codes"
       out=[]
       for letter in string:
              code = ord(letter)
              out = out + [code]
       return out 

print(encryptor("iman"))

       




       
