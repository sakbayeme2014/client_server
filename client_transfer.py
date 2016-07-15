#!/usr/bin/env python

import socket
import sys

if len(sys.argv) <=1:
 print "Usage : client_transfer.py <ip address> <file to receiving>"
 print "Usage : client_transfer.py <localhost> </var/receive.txt>"
 exit()

nbytes = 4096

def client_transfer():

 host = sys.argv[1]
 port = 50000
 socket_object = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 socket_object.connect((host , port))
 socket_object.send("hi server")
 file_object = open(sys.argv[2], "wb")
 print "file open"
 while True:
  print ("receiving data ...")
  info_object = socket_object.recv(nbytes)
  print ("info_object = %s" , (info_object))
  if not info_object:
   break
  file_object.write(info_object)

 file_object.close()
 print ("Successfully get the file")
 socket_object.close()
 print("Connection close")

client_transfer()
