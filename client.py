import socket

PORT = 8082
HEADER = 64

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostbyname(socket.gethostname())

ADDR = (host_name,PORT)

s.connect(ADDR)
print("Connected to the chat server")
print("----------------------------------------------------------------------")

while 1:
	incoming_message = s.recv(1024)
	incoming_message=incoming_message.decode()
	print("Server: ",incoming_message)
	message = input(str(">>"))
	message = message.encode()
	s.send(message)
	print("*Message sent")
