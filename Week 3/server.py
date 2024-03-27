import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 12345
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Waiting for connections...")
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)
pesan = client_socket.recv(1024).decode()
print("Received message:", pesan)
jumlah_karakter = len(pesan)
response = "Jumlah karakter pada pesan: " + str(jumlah_karakter)
client_socket.sendall(response.encode())
client_socket.close()
server_socket.close()
