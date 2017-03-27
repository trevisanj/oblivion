"""
Based on https://pymotw.com/2/socket/tcp.html
"""

import socket
import sys
import time

ADDRESS = "10.0.0.1"
PORT = 10000

# Connect the socket to the port on the server given by the caller
server_address = (ADDRESS, PORT)



# sock.connect(server_address)


while True:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print >> sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    try:
        message = ""
        while not message.endswith("(eof)"):
            message += sock.recv(99999)

        data = message[:-5].strip()
        if data == "(finished!)":
            print("Finished!")
            break


        print("Data: '{}'".format(data))

        print("Processing...")
        time.sleep(2)
        print("...done!")


    finally:
        sock.close()