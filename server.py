import socket

PORT = 8082
HEADER = 64

x = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
host_address = socket.gethostbyname(socket.gethostname())
host_name = socket.gethostname()
ADDR = (host_address,PORT)

print(host_name, "started the server with address ",host_address)

x.bind(ADDR)
print("Server binding to host", host_address, "and port", PORT, "successful")
print("Server is waiting for incoming connections...")

x.listen(1)

connection,address = x.accept()

print(address,"has connected to the server and is now online")
print("----------------------------------------------------------------")

while 1:
	display_msg = input(str(">>"))
	display_msg = display_msg.encode()
	connection.send(display_msg)
	print("*Message sent")
	in_msg = connection.recv(1024)
	in_msg = in_msg.decode()
	print("Client: ",in_msg)


