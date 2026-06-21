import socket
import json
import datetime

def tratar_requisicao(requisicao, objetos):
    req_line = requisicao['Request']
    host = requisicao['Host']
    conn = requisicao['Conn']
    user_agent = requisicao['User-agent']

    req_line = req_line.split(" ")

    method = req_line[0]
    file = req_line[1]
    version = req_line[2]
    code = ""


    if file in objetos:
        code = "200 OK"
    else:
        code = "404 not found"

    date = str(datetime.datetime.now())

    resposta = {
        "State":version + " " + code,
        "Conn": "close",
        "Date": date,
        "Server": "Linux mint",
        "Last modified": date,
        "Content-type": "text/html"
    }

    return resposta

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
    resposta = json.dumps(resposta)

    conn_socket.send(resposta.encode())
    conn_socket.close()


