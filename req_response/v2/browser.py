import socket
import json

server_ip = 'localhost'
server_port = 45000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

requisicao = {
    "Request": "GET" + " " + "/somedir/page.html" + " " + "1.1",
    "Host": server_ip,
    "Conn": "close",
    "User-agent": "brave"
}



mensagem = json.dumps(requisicao)

client.send(mensagem.encode())

resposta = client.recv(1024).decode()

print(resposta)
