import socket
import threading

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"
#SERVER = '192.168.0.118' hard coded ip
SERVER = socket.gethostbyname(socket.gethostname()) #dynamic ip
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(clientsocket, address):
    print(f"[NEW CONNECTION] {address} connected")
    connected = True
    while connected:
        msg_length = clientsocket.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = clientsocket.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{address}] {msg}")
            clientsocket.send("Hey, We recieved your message!".encode(FORMAT))

    # clientsocket.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening to {SERVER}")
    while True:
        clientsocket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(clientsocket,address))
        thread.start()
        print(f"[ACTIVE CONNETIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()
