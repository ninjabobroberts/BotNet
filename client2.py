#Client
import sys
import os
import socket
import time
import random

Host = host
Port = 12345
s = socket.socket()

def server_connect():
    s.connect((Host, Port))
    i = s.recv(1024)
    name = "Zombie" + i
    s.send(name, " : Here")
    time.sleep(ramdom.randint(1,50))
