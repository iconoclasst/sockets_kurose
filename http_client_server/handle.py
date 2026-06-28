import datetime

def verify_file(file):
    try:
        with open(file, 'r') as f:
            return True
    except IOError:
        return False

def handle_request(request, conn_socket, addr):
    req_line = request['Request-line']
    req_line = req_line.split(" ")
    filename = req_line[1]

    if verify_file(filename):
        file = open(filename, 'rb')
        kar = file.read(4096)

        conn_socket.sendall(kar)
        print(f'File sent to {addr}')
        file.close()
    else:
        print(f'Error! the file {filename} was not found.')

def response(request):
    req_line = request['Request-line']
    host = request['Host']
    conn = request['Conn']
    user_agent = request['User-agent']

    req_line = req_line.split(" ")

    method = req_line[0]
    file = req_line[1]
    version = req_line[2]

    date = str(datetime.datetime.now())

    if verify_file(file):
        code = '200 ok'
    else:
        code = '404 not found'

    answer = {
        "State":version + " " + code,
        "Conn": "close",
        "Date": date,
        "Server": "Linux mint",
        "Last modified": date,
        "Content-type": "text/html"
    }

    return answer