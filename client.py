import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((socket.gethostname(), 1234))

full_msg = ''

while True:
    msg = soc.recv(1024)
    if len(msg) <=0 :
        break 
    full_msg += msg.decode("utf-8")
    
print(full_msg)