#!/usr/bin/python

import socket
from time import ctime
 
HOST = 'localhost'
PORT = 10012
BUFSIZE = 1024
ADDR = (HOST,PORT)
  
tcpSock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSock.connect(ADDR)   
while True:
    data = raw_input(">")
    if not data:
        break
    tcpSock.send(data)                       
    data = tcpSock.recv(BUFSIZE)                                
    if not data:
        break                                                    
    print data                                                             
tcpSock.close()
