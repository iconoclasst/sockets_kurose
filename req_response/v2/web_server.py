import socket
import json

def tratar_requisicao(requisicao, objetos):
    req_line = requisicao['Request']
    host = requisicao['Host']
    conn = requisicao['Conn']
    user_agent = requisicao['User-agent']

    req_line = req_line.split(" ")

    method = req_line[0]
    file = req_line[1]
    version = req_line[2]

    if file in objetos:
        return "OK"
    return "404 not found"



ip = 'localhost'
port = 45000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print(f"Listening on {ip}:{port}")

objects = ['/somedir/page.html', '/somerdir/index.html', '/images/image.png']

while True:
    conn_socket, addr = server.accept()
    requisicao = json.loads(conn_socket.recv(1024).decode())

    resposta = tratar_requisicao(requisicao, objects)
    
    # resposta = json.dumps(requisicao)

    conn_socket.send(resposta.encode())
    conn_socket.close()


