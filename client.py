import socket
import sys


ENCODING = 'utf-8'
s = socket.socket()
s.connect(('127.0.0.1', 6666))


def send(message: str, ):
    if message == '': return
    s.send(f'{len(message.encode(ENCODING))} {message}'.encode(ENCODING))


try:
    while 1:
        send(input('type a message...\n'))
except KeyboardInterrupt:
    s.close()
    sys.exit()
