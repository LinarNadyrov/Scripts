#!/usr/bin/python3
# coding: utf-8 

import socket
import os

def CheckPort(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

ADDRESS = "127.0.0.1"
PORT = 389
SERVICE_STOP = "sudo systemctl stop keepalived.service"
SERVICE_START = "sudo systemctl start keepalived.service"

#print(CheckPort(ADDRESS, PORT))

status_keepalived = os.system("systemctl is-active --quiet keepalived.service")
#print(status_keepalived )

# ADDRESS and PORT unreachable, stop SERVICE
if CheckPort(ADDRESS, PORT) == False:
        os.system(SERVICE_STOP)

# ADDRESS and PORT run
if CheckPort(ADDRESS, PORT) == True:
         # SERVICE unreachable, start SERVICE
         if status_keepalived != 0:
           os.system(SERVICE_START) 
