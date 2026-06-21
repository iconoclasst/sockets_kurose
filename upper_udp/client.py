import socket

server = 'localhost'
port = 12000
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = input("")

client.sendto(mensagem.encode(), (server, port))

resposta, _ = client.recvfrom(2048)

print(resposta.decode())

client.close()
