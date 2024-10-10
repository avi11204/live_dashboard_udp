import socket

# Client setup
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Connected to the server.")

while True:
    # Client sends a message to the server
    message = input("Enter your message (type 'exit' to close): ")
    if message == 'exit':
        break
    clientSocket.send(message.encode())
    
    # Receive acknowledgment from the server
    server_response = clientSocket.recv(1024).decode()
    print(f"Server response: {server_response}")

clientSocket.close()
