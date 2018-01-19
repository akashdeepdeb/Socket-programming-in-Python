import socket

s = socket.socket()
print('Socket successfully created')

port = 6000
s.bind(('', port))
print("socket binded to %s" %port)
s.listen(5)
print("socket is listening")

message = 'Hey'

while True:
	c, addr = s.accept() #receives address from client
	print(addr)
	c.send(message.encode('utf-8'))
	#data = c.recv(1024)
	#print(data)
	c.close()

