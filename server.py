import socket


BUFFER = 2
ADDRESS = ('127.0.0.1', 6666)
ENCODING = 'utf-8'
s = socket.socket()
s.bind(ADDRESS)
s.listen()
conn, addr = s.accept()

full_msg_bytes = ''.encode(ENCODING)
message_encoded = ''.encode(ENCODING)

message = ''
len_msg = 0
messages = []

print(f'Server started with addr: {ADDRESS}')
while 1:
    msg = conn.recv(BUFFER)
    if len(msg) <= 0:
        break
    full_msg_bytes += msg
    args = full_msg_bytes.split(' '.encode(ENCODING), 1)
    # receive length of msg
    if len(args) >= 2:
        len_msg = int(args[0].decode(ENCODING))
        message_encoded += args[1]
        # receive msg
        state = True
        while state:
            received = conn.recv(BUFFER)
            message_encoded += received
            if len(message_encoded) >= len_msg:
                message = message_encoded[:len_msg].decode(ENCODING)
                print(f'captured message: "{message}"')
                messages.append(message)

                full_msg_bytes = ''.encode(ENCODING)
                message_encoded = ''.encode(ENCODING)

                message = ''
                len_msg = 0

                state = False
                break

print('all messages:')
print(messages)
