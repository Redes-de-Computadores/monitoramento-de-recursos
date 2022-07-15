import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(), 1234))
soc.listen(5)

while True: 
    clientsocket, adress = soc.accept()
    print(f"Connection from {adress} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.send(bytes("\nHello Wrld! -socket", "utf-8"))
    clientsocket.close()
