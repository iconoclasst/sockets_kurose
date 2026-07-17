import os
import sys
import datetime

def verify(filename):
    try:
        with open(filename, 'r') as f:
            return True
    except:
        return False
    
def handle(message):
    request_line = message['Request-Line'].split(' ')
    method = request_line[0]
    filename = request_line[1]
    version = request_line[2]

    if verify(filename):

        size = os.path.getsize(filename)

        date = str(datetime.datetime.now())

        if verify(filename):
            code = '200 ok'
        else:
            code = '404 not found'

    header = {
        "State":version + " " + code,
        "Conn": "close",
        "Date": date,
        "Server": "Linux mint",
        "Last modified": date,
        "Content-type": "text/html",
        'Size': str(size)
    }


    size_header = sys.getsizeof(header)

    return header, str(size_header)

def send_file(message, conn):
    request_line = message['Request-Line'].split(' ')
    filename = request_line[1]

    size = os.path.getsize(filename)

    file = open (filename, 'rb')
    bfile = file.read(size)

    conn.send(bfile)
    print('File sent')

    file.close()

    
