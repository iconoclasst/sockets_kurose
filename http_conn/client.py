import socket
import json

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

file = open(filename,'wb')
data = client.recv(4096)
file.write(data)

file.close()
client.close()
