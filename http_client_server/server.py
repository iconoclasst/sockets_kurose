import socket
import json
import datetime
import handle
import struct

ip, port = 'localhost', 38300

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print(f'Listen on {ip}:{port}')
while 1:
    conn_socket, addr = server.accept()
    request = json.loads(conn_socket.recv(1024).decode())

    try:
        answer = handle.response(request)
        header = json.dumps(answer).encode()

        conn_socket.sendall(struct.pack('!I', len(header)))
        conn_socket.sendall(header)
        handle.handle_request(request, conn_socket, addr)
    except:
        print(f'Error')
    
    conn_socket.close()

server.close()