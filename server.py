import socket
import threading

PORT = 5050
#SERVER = '192.168.0.118' hard coded ip
SERVER = socket.gethostbyname(socket.gethostname()) #dynamic ip
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(clientsocket, address):
    pass
def start():
    server.lissten()
    while True:
        clientsocket, address = server.accept()

print("[STARTING] server is starting...")
start()
