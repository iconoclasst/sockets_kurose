import socket
import json

server_ip = 'localhost'
server_port = 45000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

requisicao = {
    "Request": "GET" + " " + "/somedir/pagae.html" + " " + "1.1",
    "Host": server_ip,
    "Conn": "close",
    "User-agent": "brave"
}



mensagem = json.dumps(requisicao)

client.send(mensagem.encode())

resposta = json.loads(client.recv(1024).decode())

print(resposta)
