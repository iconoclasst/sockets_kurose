import socket
import json
from ruido import aplicar_ruido

ip, port = 'localhost', 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print(f'Listening on {ip}:{port}')
while 1:
    conn_socket, addr = server.accept()
    mensagem = json.loads(conn_socket.recv(1024).decode())

    resposta = aplicar_ruido(mensagem)

    conn_socket.send(str(resposta).encode())
    print(f"idade com ruído enviada para {addr}")
    conn_socket.close()

