from p2p import *

if __name__ == '__main__':
	# Set IP address to local IP address
	ip = socket.gethostbyname(socket.gethostname())
	port = int(input("Connect to which port number: "))
	OpenConnection(port)