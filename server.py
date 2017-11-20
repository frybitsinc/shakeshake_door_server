#!/usr/bin/env python3
import socket
import doorlock

# Server IP and port number.
ip_addr = '192.168.123.104'
port = 50100

RECV_BYTES = 16

# Create a server socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding address.
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip_addr, port))
print('Server is running at {}:{}'.format(ip_addr, port))
print('Ctrl + C to stop server.\n')
# Listen clients.
sock.listen(1)

try:
    while 1:
        # Wait for a client.
        print('Waiting for connection ...')
        conn, cli = sock.accept()
        print('/' + '=' * 70 + '\\')
        print('New client connected: {}:{}'.format(cli[0], cli[1]))
        # Receive messages.
        rec = conn.recv(RECV_BYTES)
        # Receive and response until connection closed.
        while len(rec) != 0:
            # Response to the client.
            if rec == b'true':
                print('Authentication success.')
                doorlock.unlock(True)
            elif rec == b'false':
                print('Authentication failed.')
                doorlock.unlock(False)
            conn.send(b'RECEIVED\n')
            rec = conn.recv(RECV_BYTES)
        # Connection closed.
        print('Connection closed.')
        print('\\' + '=' * 70 + '/')
        conn.close()
except KeyboardInterrupt:
    print('\nStop server.')

sock.close()
