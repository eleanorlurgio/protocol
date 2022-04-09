# p2p.py>

import random
from socket import *
from email import message
import sys
from threading import Thread
import socket
from time import sleep, time

# def InitialiseClient():

# def InitialiseServer():

BUFFER_SIZE = 1024

def ClientSend(destination_IP, destination_port):
    # Create a UDP socket
    UDP_IP_ADDRESS = destination_IP
    UDP_PORT_NO = destination_port

    # Request message from user client
    Message = str.encode("request photo")

    # Create a socket with a 1s timeout
    clientSock=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    try:
        clientSock.connect((UDP_IP_ADDRESS, UDP_PORT_NO))
    except e:
        print("HereEeeeeeeeee")
        print(e)
    print(clientSock)
    clientSock.settimeout(1.0)


    # Send data to client
    print ('Ping %d %s' % (1,Message.decode()))

    while True:
         # Send the message using the clientSock
        clientSock.send(Message)

        # Receive response
        print ('waiting to receive')

        # Get the response & extract data
        try:
            data = clientSock.recvfrom(BUFFER_SIZE)
        except TimeoutError:
            print("timeout")
            sleep(0.1)
            continue
        except ConnectionResetError:
            print("server not up")
            sleep(0.1)
            continue
        break
    message = data[0]
    address = data[1]
    print ('CLIENT: received "%s"' % message.decode())

    
    print ('closing socket')
    # Close the socket
    clientSock.close()

# Listen for incoming requests
def ClientReceive(source_IP, source_port):
    # Create a UDP socket
    # Use of SOCK_DGRAM for UDP packets
    serverSocket = socket.socket(family=AF_INET, type=SOCK_DGRAM)

    # Assign IP address and port number to socket
    serverSocket.bind((source_IP, source_port))

    while True:
        # Receive the client packet along with the address it is coming from
        print("ahdjawdklaw")
        connection = serverSocket.recvfrom(BUFFER_SIZE)
        message = connection[0]
        address = connection[1]

        # Set message to the data to be sent back
        messageA = str.encode("PHOTO.jpeg")

        # The server responds
        print("                                     SERVER: "+str(messageA.decode()))
        serverSocket.sendto(messageA, address)

def Header():

    return

def Packet(buffer, header, message):
    packet = [header, message]
    return packet
    

# The connection is defined by a tuple (source IP, source port, destination IP, destination port)
def OpenConnection(source_IP, source_port, destination_IP, destination_port):
    Thread(target = ClientReceive, args=(source_IP, source_port)).start()
    Thread(target = ClientSend, args=(destination_IP, destination_port)).start()
