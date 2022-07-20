import socket

from numpy import full

HEADERSIZE = 10

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((socket.gethostname(), 1234))


while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = soc.recv(16)
        if new_msg:
            print(f"new message lenght: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg rcvd!")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
        
    print(full_msg)