import socket
import threading
import time

SERVER = "192.168.1.35"
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

def resource_request():
    while True:     
        time.sleep(1) 

        print('''
        For a server resource checking choose:

        1.RAM Memory
        2.CPU
        3.GPU
        0.Exit
        ''')
        chosen_resource_option = int(input('What\'s ur choice? '))
        
        if(chosen_resource_option > 0 and chosen_resource_option < 4):
            send(f"rsrc={chosen_resource_option}")
            resource_type(chosen_resource_option)

        elif(chosen_resource_option == 0):
            exit()
            break

        else:
            err()

def resource_type(chosen_resource_option):
    resource = ''
    while True:
        time.sleep(1)
        if(chosen_resource_option == 1):
            resource = 'RAM Memory'

        elif (chosen_resource_option == 2):
            resource = 'CPU'

        elif (chosen_resource_option == 3):
            resource = 'GPU'

        print(f'''
            What type information u want to see:

            1.Total of {resource}
            2.{resource} available
            3.{resource} usage percent
            4.{resource} used
            5.{resource} free
            0.Voltar
            ''')
        chosen_type = int(input('What\'s ur choice? '))
        
        if(chosen_type > 0 and chosen_type < 4):
            send(f"type={chosen_type}")

        elif(chosen_type == 0):
            print('Getting back to the Menu...')
            break

        else:
            err()

def init():
    send_author()
    resource_request()
    resource_type()

def err():
    print('''
    ===================
      Invalid Option!
    ===================
    ''')
    time.sleep(1)

def exit():
    print('''
    ============
      Bye Bye!
    ============
    ''')
    time.sleep(1)

def start():
    print('''
    =====================================
    Welcome to Server Resources Monitorer
    =====================================
    ''')
    thread1 = threading.Thread(target=handle_messages)
    thread2 = threading.Thread(target=init)
    thread1.start()
    thread2.start()

start()