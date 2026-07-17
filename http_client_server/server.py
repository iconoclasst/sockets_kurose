import socket
import json
import handle


IP, PORT = 'localhost', 55000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))

server.listen(1)

while 1:
    conn, addr = server.accept()
    print(f'Conn with {addr}')

    message = json.loads(conn.recv(1024).decode())

    header, size_header = handle.handle(message)

    conn.send(size_header.encode())

    conn.send(json.dumps(header).encode())

    handle.send_file(message, conn)
    
    conn.close()

server.close()