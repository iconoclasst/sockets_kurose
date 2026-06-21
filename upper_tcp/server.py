import socket

ip = 'localhost'
port = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", port))
server.listen(1)

print(f"listening on {ip}:{port}")

i = 1
while True:
    conn_socket, addr = server.accept()
    mensagem = conn_socket.recv(1024)
    resposta = mensagem.decode().upper()

    conn_socket.send(resposta.encode())
    print(f"Envio {i} feito")
    i+=1

    conn_socket.close()

