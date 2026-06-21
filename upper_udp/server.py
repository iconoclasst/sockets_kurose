import socket

ip = 'localhost'
port = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("", port))

print(f"listening on {ip}:{port}")

i = 1
while True:

    mensagem, caddress = server.recvfrom(2048)

    resposta = mensagem.decode().upper()
    server.sendto(resposta.encode(), caddress)
    print(f"Envio {i} feito")
    i+=1

