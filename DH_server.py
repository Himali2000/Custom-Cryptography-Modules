import socket, pickle
import random

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, ip_address = s.accept()
print("\nConnected with ", ip_address)

while 1:
    data = connection.recv(4096)
    if not data:
        break
    data_arr = pickle.loads(data)
    print(data_arr)
    XB = random.randint(1,100)
    YB = (data_arr[1]**XB) % data_arr[0]
    print("\nGenerated key using sender's public key at receiver side: ")
    recieved_key = (data_arr[2]**XB) % data_arr[0]
    print(recieved_key)
    data_arr[2] = YB
    data_string = pickle.dumps(data_arr)
    connection.send(data_string)

connection.close()
