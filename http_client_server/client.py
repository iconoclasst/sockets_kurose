import socket
import struct
import json

def receiv(client, n):
    data = b''
    while len(data) < n:
        try:
            packet = client.recv(n - len(data))
        except:
            print('No connection')
        data += packet
    return data

ip, port = 'localhost', 38300

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

filename = 'index.html'

message = {
    'Request-line': 'GET' + " " + filename + " " + "1.1",
    'Host': ip,
    'Conn': 'close',
    'User-agent': 'brave'
}

client.send(json.dumps(message).encode())

size = struct.unpack("!I", receiv(client, 4))[0]
response_header = json.loads(receiv(client, size).decode())
print(response_header)

try:
    file = open(filename,'wb')
    data = client.recv(4096)
    file.write(data)
    print('File received!')
except:
    print('Error! file not received')

file.close()
client.close()
