import socket
import json

IP, PORT = 'localhost', 55000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

filename = 'index.html'

message = {
    'Request-Line': 'GET' + ' ' + filename + ' ' + '1.1',
    'Host': IP,
    'Connection': 'close',
    'User-agent': 'Brave'
}

message = json.dumps(message)
client.send(message.encode())

size_header = client.recv(4).decode()
print(size_header)
size_header = int(size_header)

# print(type(size_header))
# size_header = int(size_header)
header = json.loads(client.recv(size_header))
print(header)

size = int(header['Size']) 
print(size)

file = open('index.html', 'wb')
data = client.recv(size)
file.write(data)
file.close()

client.close()