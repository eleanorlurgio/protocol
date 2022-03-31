# p2p.py>

import random
from socket import *
from email import message
import sys
from threading import Thread
import socket

# def InitialiseClient():

# def InitialiseServer():

def ClientSend(ip, port):
    # Create a UDP socket
    UDP_IP_ADDRESS = ip
    UDP_PORT_NO = port

    # Request message from user client
    Message = str.encode("request photo")

    # Create a socket with a 1s timeout
    clientSock=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    clientSock.settimeout(1.0)

    for i in range(0,10):
        # Send data to fridge client
        print ('Ping %d %s' % (i,Message.decode()))

        try:
            # Send the message using the clientSock
            sent=clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
            # Receive response
            print ('waiting to receive')

            # Get the response & extract data
            data = clientSock.recv(1024)
            print ('CLIENT: received "%s"' % data.decode())
        except socket.timeout as inst:
            # Handle timeouts
            print('Request timed out')
    print ('closing socket')
    # Close the socket
    clientSock.close()

# Listen for incoming requests
def ClientReceive(ip, port):
    # Create a UDP socket
    # Use of SOCK_DGRAM for UDP packets
    serverSocket = socket.socket(family=AF_INET, type=SOCK_DGRAM)

    # Assign IP address and port number to socket
    serverSocket.bind((ip, port))

    while True:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)

        # Set message to the data to be sent back
        message = str.encode("PHOTO.jpeg")

        # The server responds
        print("                                     SERVER: "+str(message.decode()))
        serverSocket.sendto(message, address)


def OpenConnection():
    Thread(target = ClientSend, args=('127.0.0.1', 12000)).start()
    Thread(target = ClientReceive, args=('127.0.0.1', 12000)).start()