#!/usr/bin/python
#compst.io, comp.st

import os, sys, urllib

def main():
    if len(sys.argv) == 2:
        ac = sys.argv[1]
        print "[*] Uploading file", ac
        os.system('cat %s | curl comp.st -Fp=\<-' % (ac))

        if sys.argv[1] == '--read':
            print "Reading", sys.argv[2]
            url = sys.argv[2]
            data = urllib.urlopen(url)
            content = data.read()
            print content

    else:
        return usage()

def usage():
    print """
Author: eitenne { Usage: <filename.jpg.png.txt.etc> }
Hosts: compst.io, comp.st

EXAMPLES:
  ./compst.py <filename>
  ./compst.py --read https://compst.io/1337
"""

main()
