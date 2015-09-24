import socket
import time

# Create a TCP/IP socket
sock = socket.create_connection(('137.112.218.138', 2000))

try:
    sock.sendall("1".encode())
    print("LED On")
    time.sleep(2.0)
    sock.sendall("0".encode())
    print("LED Off")
    time.sleep(2.0)
    sock.sendall("1".encode())
    print("LED On")
    time.sleep(2.0)
    sock.sendall("0".encode())
    print("LED Off")

    amount_received = 0
    while amount_received < 15:
        data = sock.recv(16)
        amount_received += len(data)
        print("received " + str(data))

finally:
    sock.close()
