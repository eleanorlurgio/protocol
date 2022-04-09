from p2p import *

# The connection is defined by a tuple (source IP, source port, destination IP, destination port)
# def OpenConnection(client1_IP, client1_port, client2_IP, client2_port):
#     Thread(target = ClientSend, args=(client1_IP, client1_port)).start()
#     Thread(target = ClientReceive, args=(client2_IP, client2_port)).start()

if __name__ == '__main__':
	# Set IP address to local IP address
	# ip = socket.gethostbyname(socket.gethostname())
	print(socket.gethostbyname(socket.gethostname()))
	source_IP = "0.0.0.0" #socket.gethostbyname(socket.gethostname())
	source_port = 12500
	destination_IP = "localhost" #socket.gethostbyname(socket.gethostname())
	destination_port = 12501
	# port = int(input("Connect to which port number: "))
	# Thread(target = OpenConnection, args=(source_IP, source_port, destination_IP, destination_port)).start()
	OpenConnection(source_IP, source_port, destination_IP, destination_port)
    # Thread(target = OpenConnection, args=(client1_IP, client1_port, client2_IP, client2_port)).start()