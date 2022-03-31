# UDPPingerClient.py
# We will need the following module to generate randomized lost packets
from email import message
import sys
import socket

# Create a UDP socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 12000
Message = b"Hello, Server"

# create a socket with a 1s timeout.
clientSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.settimeout(1.0)

for i in range(0,10):
	# Send data
	print ('Ping %d %s' % (i,Message))
	try:
        ## sent the Message using the clientSock
		sent=clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
		# Receive response
		print ('waiting to receive')
		##get the response & extract data
        ##
		data = clientSock.recv(1024)
		print ('received "%s"' % data)
	except socket.timeout as inst:
		## handle timeouts
		print('Request timed out')
print ('closing socket')
##close the socket
clientSock.close()