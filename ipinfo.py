#!/usr/bin/python
import urllib

def main():
    x = urllib.urlopen("http://ipinfo.io/ip") #/* Get ip address from ipinfo.io */
    ip = x.read() #/* Make ip as a varible */
    z = urllib.urlopen("http://ipinfo.io/country") #/* Get country from ipinfo.io */
    country = z.read() #/* Make country as a varible */
    d = urllib.urlopen("http://ipinfo.io/hostname") #/* Get hostname from ipinfo.io */
    hostname = d.read() #/* Make hostname as a varible */
    q = urllib.urlopen("http://ipinfo.io/city") #/* Get city from ipinfo.io */
    city = q.read() #/* Make city as a varible */
    t = urllib.urlopen("http://ipinfo.io/region") #/* Get region from ipinfo.io */
    region = t.read() #/* Make region as a varible */
    
    
    print "[*] Region: %s" % (region)
    print "[*] Country: %s" % (country)
    print "[*] City: %s" % (city)
    print "[*] Hostname: %s" % (hostname)
    print "[*] Ip Address: %s" % (ip)

main()