#!/usr/bin/env python

import socket

nbytes = 1024

def server_data():

 host = "0.0.0.0"
 port = 59000
 socket_object = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 socket_object.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
 socket_object.bind((host , port))
 socket_object.listen(10)
 print "Server listening"
 conn , addr = socket_object.accept()
 print "Got connect from", addr
 while True:
  info_object = conn.recv(nbytes)
  print ("Server received", repr(info_object))
  conn.send(info_object)
  print("send", repr(info_object))
  conn.send("data sending")
  socket_object.close()

server_data()
