import socket

HOST = "127.0.0.1"
PORT = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected to server. Type 'quit' to exit.")

while True:
    msg = input("You: ")
    if msg.lower() == "quit":
        break
    client.sendall(msg.encode())
    data = client.recv(1024)
    print("Server says:", data.decode())

client.close()
