import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print('socket creation failed error %s'%(err))

port = 6000

try: 
	host_ip = socket.gethostbyaddr('10.193.31.54')[0]
except:
	socket.gaierror()
	sys.exit()

s.connect((host_ip, port))
message = 'hey'
s.send(message.encode('utf-8'))