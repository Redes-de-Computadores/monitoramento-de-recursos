import socket

HEADERSIZE = 10

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(), 1235))
soc.listen(5)

while True: 
    clientsocket, adress = soc.accept()
    print(f"Connection from {adress} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))