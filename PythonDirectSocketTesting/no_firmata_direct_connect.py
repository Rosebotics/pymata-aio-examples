'''
Example of making a direct socket connection to the WiFly.

This seems to work fine.  I've only tested this program with a WiFly connected to my computer.
I plan to try running a socket with the WiFly on an actual RedBot next.
AFTER I get a basic demo working on RedBot, then I'll try moving into pymata-aio stuff.

@author: fisherds
'''

import socket

# Create a TCP/IP socket
sock = socket.create_connection(('137.112.218.165', 2000))

try:
    sock.sendall("Hello World".encode())
    
    amount_received = 0
    while amount_received < 10:
        data = sock.recv(16)
        amount_received += len(data)
        print("received " + str(data))

finally:
    sock.close()