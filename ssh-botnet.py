#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, string, time, paramiko
os.system('clear')

print """
   ╭─────────────────────────────────────╮
   │                                     │
   │     Author: Eitenne                 │
   │     Script: SSH Botnet              │
   │                                     │
   ╰─────────────────────────────────────╯
"""

target = raw_input("[127.0.0.1]~[~]: ")

###################
### C O N F I G ###
###################

cmd = "some command execution line goes here a good way of exploiting multiple boxes at once! :D"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

servers = []
ssh.connect('127.0.0.1', username='root', password='pass123') 

stdin, stdout, stderr = ssh.exec_command(cmd)
stdin.flush()

print stdout.readlines()
