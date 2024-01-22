def decryptor(Codes):
       "This function convert a list of ASCII codes to a string"
       out = ""
       for code in Codes:
              out = out + chr(code)
       return out 

print(decryptor([105,109,97,110]))





       
