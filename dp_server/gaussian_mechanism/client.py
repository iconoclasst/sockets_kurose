import socket
import json

dst, port = 'localhost', 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((dst, port))

idade = input('Digite sua idade: ')
nivel = input('Nivel de privacidade:\nforte- 1\nmedia- 2\nfraca- 3\n:')

mensagem = {
    'idade':idade,
    'nivel':nivel
}

mensagem = json.dumps(mensagem)

client.send(mensagem.encode())
resposta = client.recv(1024).decode()

print(resposta)