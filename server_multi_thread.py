#!/usr/bin/env python

import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import sys

if len(sys.argv) <=1:
 print "Usage : ./server_multi_thread.py <ip address> </path/file to transfer>"
 print "Usage : ./server_multi_thread.py 0.0.0.0 </tmp/receive>"
 exit()

IP = sys.argv[1]
PORT = 60000
BUFFER_SIZE = 4096

class ClientThread(Thread):
 def __init__(self, ip, port, sock):
  Thread.__init__(self) 
  self.ip = ip
  self.port = port
  self.sock = sock

 def ip_file(self, ip):
  self.ip = ip
 def port_file(self, port):
  self.port = port 
 def sock_file(self, sock):
  self.sock = sock
 def tcp_sock(sock, tcpsockfile):
  self.tcpsockfile = tcpsockfile
 def file_open(self, file_object):
  self.file_object = file_object
 def cont_file(self, contents):
  self.contents = contents
 def conn_file(self, conn):
  self.conn = conn
 def new_thread(self, newthread):
  self.newthread = newthread
 def thread_file(self, thread):
  self.thread = thread
 
 def run(self):
  file_object = open(sys.argv[2] , "rb") 
  while True:
   contents = file_object.read(BUFFER_SIZE)
   while(contents):
    self.sock.send(contents)
    print('send ', repr(contents))
    contents = file_object.read(BUFFER_SIZE)
   if not contents:
    file_object.close()
    self.sock.close()
    break


server_object = ClientThread("ip" , "port", "sock" )
server_object.tcp_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_object.tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_object.tcp_sock.bind((IP , PORT))
server_object.thread_file = []

while True:
 server_object.tcp_sock.listen(10)
 print "Waiting for incoming connections..."
 (server_object.conn_file, (server_object.ip_file, server_object.port_file)) = server_object.tcp_sock.accept()
 print "Got connection from", (server_object.ip_file , server_object.port_file)
 server_object.new_thread = ClientThread(server_object.ip_file, server_object.port_file, server_object.conn_file)
 print "New thread started for "+server_object.ip_file+":"+str(server_object.port_file)
 server_object.new_thread.start()
 server_object.thread_file.append(server_object.new_thread)
   
for j in server_object.thread_file:
 j.join()


 
 


 
  
 
 
   
