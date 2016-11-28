#!/usr/bin/python
import socket
from time import ctime

HOST = ""
PORT = 10012
ADDR = (HOST,PORT)     
BUFSIZE = 1024
      
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)         
while True:
    print "Waiting for connection..."
    conn,addr = s.accept()
    print "...connection from:",addr
    while True:
        data = conn.recv(BUFSIZE)
        if not data:
            break
        conn.send('[%s] %s'%(ctime(),data))
        print [ctime()],':',data
conn.close()
s.close()
