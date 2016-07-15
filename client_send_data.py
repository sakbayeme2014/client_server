#!/usr/bin/env python

import socket

nbytes = 1024

def client_data():

 host = "192.168.1.13"
 port = 59000
 socket_object = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 socket_object.connect((host , port))
 while True:
  msg_object = raw_input()
  if msg_object == "exit":
   break
  socket_object.send(msg_object)
 socket_object.close()

client_data()
