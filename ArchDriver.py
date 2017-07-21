#!/usr/bin/python
#Author: Eitenne

import sys, os, time

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'Fallback':
            return fallback()
        if sys.argv[1] == 'Intel':
            return intel()
        if sys.argv[1] == 'Nvidia':
            return nvidia()
        if sys.argv[1] == 'Radeon':
            return radeon()
        if sys.argv[1] == 'Mesa':
            return mesa()
    else:
           return usage()

def usage():
    print """
Usage: archdriver [Options]

EXAMPLES:
  ./ArchDriver.py Fallback
  ./ArchDriver.py Intel
  ./ArchDriver.py Nvidia
  ./ArchDriver.py Radeon
  ./ArchDriver.py Mesa

DOC:
    Once you have installed the needed drivers
    you will need to -Syyu and then reboot
"""

def fallback():
    print "[!] Installing Fallback drivers"
    os.system('pacman -S xf86-video-vesa')

def intel():
    print "[!] Installing Intel drivers"
    os.system('pacman -S xf86-video-intel')

def nvidia():
    print "[!] Installing Nvidia drivers"
    os.system('pacman -S xf86-video-nouveau')

def radeon():
    print "[!] Installing Radeon Mesa"
    os.system('pacman -S xf86-video-ati')

def mesa():
    print "[!] Installing Mesa drivers"
    os.system('pacman -S mesa mesa-libgl')
    os.system('pacman -S lib32-mesa lib32-mesa-libgl')

main()
