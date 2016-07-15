#!/usr/bin/env python

import socket
import sys

if len(sys.argv) <=1:
 print "Usage : ./client_thread.py <ip address> </path/file>"
 print "Usage : ./client_thread.py <192.168.0.12> </tmp/file>"
 exit()

BUFFER_SIZE = 4096

def client_thread():

 IP = sys.argv[1]
 PORT = 60000
 client_object = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 client_object.connect((IP , PORT))

 file_object = open(sys.argv[2], "wb")
 print " file open "
 while True:
  print("receiving data")
  contents = client_object.recv(BUFFER_SIZE)
  print('contents=%s' , (contents))
  if not contents:
   file_object.close()
   print 'file close()'
   break
  file_object.write(contents)

 print("success file get")
 client_object.close()

client_thread()


