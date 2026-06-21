import socket
import json

server_ip = 'localhost'
server_port = 45000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

requisicao = {
    "method": "GET",
    "url": server_ip + "/" + "page.html",
    "version": "1.1"
}

mensagem = json.dumps(requisicao)

client.send(mensagem.encode())

resposta = json.loads(client.recv(1024).decode())

print(resposta)