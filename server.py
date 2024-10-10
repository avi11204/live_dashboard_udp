import socket
import threading

# Server setup
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # Allow up to 5 simultaneous connections
print('The server is ready to receive multiple clients')

def handle_client(connectionSocket, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            # Receive and display data from the client
            message = connectionSocket.recv(1024).decode()
            if not message:
                break
            print(f"Received from {addr}: {message}")
            # Server can send acknowledgment back to the client (optional)
            connectionSocket.send(f"Message received: {message}".encode())
        except:
            break
    print(f"Connection with {addr} closed")
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
