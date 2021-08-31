class RailFence:
    # Encryption function
    def railencrypt(self, user_string, key):
        row = 0
        x = 0
        m =[[0] * (len(user_string)) for i in range(key)]
        for colm in range(len(user_string)):
            m[row][colm] = user_string[colm]
            if x == 0:
                if row == (key-1):
                    x = 1
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    x = 0
                    row += 1
                else:
                    row -= 1
        result = []
        for i in range(key):
            for j in range(len(user_string)):
                if m[i][j] != 0:
                        result.append(m[i][j])
        return "". join(result)

    # Decryption function
    def raildecrypt(self, user_string, key):
        row , x = 0 , 0
        m =[[0] * (len(user_string)) for i in range(key)]
        for colm in range(len(user_string)):
            m[row][colm] = 1
            if x == 0:
                if row == (key-1):
                    x = 1
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    x = 0
                    row += 1
                else:
                    row -= 1
        result = []
        row , x = 0 , 0
        for i in range(key):
            for j in range(len(user_string)):
                if m[i][j] == 1:
                    m[i][j] = user_string[x]
                    x += 1
        for colm in range(len(user_string)):
            if m[row][colm] != 0:
                result.append(m[row][colm])
            if x == 0:
                if row == (key-1):
                    x = 1
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    x = 0
                    row += 1
                else:
                    row -= 1
        return "". join(result)


# Object creation and functions calls
user_string = input("Plain text: ")
key = int(input("Key: "))

obj = RailFence()
user_string = user_string.upper()

enc = obj.railencrypt(user_string, key)
print("Cipher text: "+ enc)
dec = obj.raildecrypt(enc, key)
print("Decipher text: "+ dec)
