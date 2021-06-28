def encryption(plaintext, key):
   cipher = ""
   for i in range(len(plaintext)):
       var = plaintext[i]
       if (var.isupper()):
           cipher += (chr((ord(var) + key - 64) % 26 + 65))
       else:
           cipher += (chr((ord(var) + key - 96) % 26 + 97))
   return cipher

def decryption(cipher, key):
    decipher = ""
    for i in range(len(cipher)):
       var = cipher[i]
       if (var.isupper()):
           decipher += (chr((ord(var) - key - 64) % 26 + 63))
       else:
           decipher += (chr((ord(var) - key - 96) % 26 + 95))
    return decipher
