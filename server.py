import socket
import threading
import time

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = []
messages = []
rsrc_request = []

def send_individual_message(connection):
    print(f"[SENDING] Sending messages to {connection['addr']}")
    for i in range(connection['last'], len(messages)):
        send_message = "msg=" + messages[i]
        connection['conn'].send(send_message.encode())
        connection['last'] = i+1
        time.sleep(0.3)

def send_message_all():
    global connections
    for connection in connections:
        send_individual_message(connection)

def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] A new user has connected by address: { addr }")
    global connections
    global messages
    name = False

    while(True):
        requestion = conn.recv(1024).decode(FORMAT)
        if(requestion):
            if(requestion.startswith("name=")):
                separate_requestion = requestion.split("=")
                name = separate_requestion[1]
                connection_map = {
                    "conn": conn, 
                    "addr": addr, 
                    "name": name, 
                    "last": 0
                }
                connections.append(connection_map)
                send_individual_message(connection_map)
            elif(requestion.startswith("rsrc=")):
                separate_requestion = requestion.split("=")
                resource = int(separate_requestion[1])
                rsrc_request.append(resource)
                print(resource)
                # send_message_all()
            elif(requestion.startswith("type=")):
                separate_requestion = requestion.split("=")
                resource_type = int(separate_requestion[1])
                rsrc_request.append(resource_type)
                print(resource_type)
            print(rsrc_request)


def start():
    print("[STARTING] Starting Socket!")
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()

start()