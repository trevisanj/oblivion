"""
Based on https://pymotw.com/2/socket/tcp.html
"""

import socket
import sys
import cPickle

ADDRESS = "10.0.0.1"
PORT = 10000

def next_line():
    # Reads observational data
    with open("data.txt") as f:
        lines = f.readlines()
    for line in lines:
        yield line

info_generator = next_line()


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (ADDRESS, PORT)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(2)

continue_serving = True
while continue_serving:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        try:
            information = info_generator.next()
        except:
            information = "(finished!)"
            # continue_serving = False

        connection.sendall(information+"(eof)")
    finally:
        connection.close()