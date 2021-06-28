# The 'plaintext' is the 'p' in cipher=ENC(p + k)%26 encryption function
# The 'key' or 'k' refers to the possible and preferable shift and its range is 1-26 (integer only)
# Typical key for Caesar cryptography is 3

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

# No key input in brute force attack
def brute(cipher):
    for iteration in range(0, 26):
        intermediate = ""
        for j in cipher:
            if (j.isupper()):
                intermediate += (chr((ord(j) + iteration - 64) % 26 + 65))
            else:
                intermediate += (chr((ord(j) + iteration - 96) % 26 + 97))
        print(intermediate)
