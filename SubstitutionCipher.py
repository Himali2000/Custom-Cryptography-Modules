# The 'plaintext' is the 'p' in cipher=ENC(p + k)%26 encryption function
# The 'key' or 'k' refers to the possible and preferable shift and its range is 1-26
# Typical key for Caesar cryptography is 3

class Caesar():

    def encryption(self, plaintext, key):
        cipher = ""
        for i in range(len(plaintext)):
            var = plaintext[i]
            if (var.isupper()):
                cipher += (chr((ord(var) + key - 64) % 26 + 65))
            else:
                cipher += (chr((ord(var) + key - 96) % 26 + 97))
        return cipher

    def decryption(self, cipher, key):
        decipher = ""
        for i in range(len(cipher)):
            var = cipher[i]
            if (var.isupper()):
                decipher += (chr((ord(var) - key - 64) % 26 + 63))
            else:
                decipher += (chr((ord(var) - key - 96) % 26 + 95))
        return decipher

    def brute(self, cipher):
        for iteration in range(0, 26):
            intermediate = ""
            for j in cipher:
                if (j.isupper()):
                    intermediate += (chr((ord(j) + iteration - 64) % 26 + 65))
                else:
                    intermediate += (chr((ord(j) + iteration - 96) % 26 + 97))
            print(intermediate)


# Here the key 'k' is 26 letters long sting

class Monoaplhabetic(Caesar):

    def convert(self, message, key):
        plaintext_alphabet = "ABCDEFCHIJKLMNOPQRSTUVWXYZ"
        message = message.upper()
        key = key.upper()
        converted = ""
        for i in range(len(message)):
            var = message[i]
            mapped = plaintext_alphabet.find(message[i])
            converted += key[mapped]
        return converted
