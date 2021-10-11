import socket, pickle
import random

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

arr = []
pnum = 14851
alpha = 23
arr.append(pnum)
arr.append(alpha)

XA = random.randint(1,100)
YA = (alpha**XA) % pnum
arr.append(YA)
data_string = pickle.dumps(arr)
s.send(data_string)
data = s.recv(4096)
data_arr = pickle.loads(data)
s.close()

print ("\nReceived", repr(data_arr))
print("\nGenerated key using reciever's public key at sender side: ")
kr = (data_arr[2]**XA) % pnum
print(kr)
