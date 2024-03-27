import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 12345
client_socket.connect((HOST, PORT))
print("Connected to server")
pesan = input("Masukkan pesan: ")
client_socket.sendall(pesan.encode())
response = client_socket.recv(1024).decode()
print("Response from server:", response)
client_socket.close()
