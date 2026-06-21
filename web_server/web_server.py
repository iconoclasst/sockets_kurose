import socket
import json

ip = 'localhost'
port = 45000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print(f"Listening on {ip}:{port}")

objects = ['page.html', 'index.html', 'image.png']

while True:
    conn_socket, addr = server.accept()
    requisicao = json.loads(conn_socket.recv(1024).decode())

    resposta = json.dumps(requisicao)

    conn_socket.send(resposta.encode().upper())
    conn_socket.close()

