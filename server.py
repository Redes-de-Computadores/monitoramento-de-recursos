import socket
import threading
import time
import monitor

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = []
resources = []

def send_resources(connection):
    print(f"[SENDING] Sending response to {connection['addr']}")
    for i in range(connection['last'], len(resources)):
        send_resource = resources[i]
        connection['conn'].send(send_resource.encode())
        connection['last'] = i+1
        time.sleep(0.3)
        resources.clear()

def handle_clients(conn, addr):
    print(f"[NEW CONNECTION] A new user has connected by address: { addr }")
    global connections
    global resources

    while(True):
        requestion = conn.recv(1024).decode(FORMAT)
        if(requestion):
            if(requestion == "1"):
                resource = monitor.mem()
            elif(requestion == "2"):
                resource = monitor.cpu()
            elif(requestion == "3"):
                resource = monitor.disk()
            
            connection_map = {
                "conn": conn,
                "addr": addr,
                "last": 0,
                "resource": resource
            }

            connections.append(connection_map)
            resources.append(resource)
            send_resources(connection_map)

def start():
    print("[STARTING] Starting Socket!")
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()

start()