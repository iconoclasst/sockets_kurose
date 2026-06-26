def verify_file(file):
    try:
        with open(file, 'r') as f:
            return True
    except IOError:
        return False

def handle_request(request, conn_socket, addr):
    filename = request['object']

    if verify_file(filename):
        file = open(filename, 'rb')
        kar = file.read(6053)

        conn_socket.send(kar)
        print(f'File sent to {addr}')
        file.close()
    else:
        print(f'Error! the file {filename} was not found.')

def response(request):
    req_line = requisicao['Request-line']
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

    answer = {
        "State":version + " " + code,
        "Conn": "close",
        "Date": date,
        "Server": "Linux mint",
        "Last modified": date,
        "Content-type": "text/html"
    }

    return answer