#!/usr/bin/env python

import socket
import sys

if len(sys.argv) <=1:
 print "Usage : python server_transfer.py <ip address> <file to send>"
 print "Usage : python server_transfer.py <localhost> </home/file.txt>"
 exit()

nbytes = 4096


def server_transfer():

 host = sys.argv[1]
 port = 50000
 socket_object = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 socket_object.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
 socket_object.bind((host , port))
 socket_object.listen(10)
 print "Server listening"
 while True:
  conn , addr = socket_object.accept()
  print "Got connection from" , addr
  info_object = conn.recv(nbytes)
  print("server received" , repr(info_object))
  file_object = open(sys.argv[2] , "rb")
  contents = file_object.read(nbytes)
  while(contents):
   conn.send(contents)
   print("send" , repr(contents))
   contents = file_object.read(nbytes)
  file_object.close()
  print("Done sending")
  conn.send("file sending ok")
  conn.close()

server_transfer()





   
