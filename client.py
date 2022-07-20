import socket
import threading
import time

SERVER = "10.2.170.35"
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_messages():
    while (True):
        msg = client.recv(1024).decode()
        separate_message = msg.split("=")
        print(separate_message[1] + ": " + separate_message[2])

def send(the_message):
    client.send(the_message.encode(FORMAT))

def send_author():
    name = input('Type ur name: ')
    send("name=" + name)

def send_message():
    while(True):   
        the_message = input()
        send("msg=" + the_message)

def init_sending():
    send_author()
    send_message()

def start():
    thread1 = threading.Thread(target=handle_messages)
    thread2 = threading.Thread(target=init_sending)
    thread1.start()
    thread2.start()

start()