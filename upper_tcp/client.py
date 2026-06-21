import socket 

ip = 'localhost'
port = 12000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

mensagem = input("")
client.send(mensagem.encode())

resposta = client.recv(1024)
print(resposta)

client.close()
