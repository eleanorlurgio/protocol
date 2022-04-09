from p2p import *

if __name__ == '__main__':
	# Set IP address to local IP address
	# ip = socket.gethostbyname(socket.gethostname())
	source_IP = '0.0.0.0'
	source_port = 12501
	destination_IP = socket.gethostbyname(socket.gethostname())
	destination_port = 12500
	# port = int(input("Connect to which port number: "))
	OpenConnection(source_IP, source_port, destination_IP, destination_port)