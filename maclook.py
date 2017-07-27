#!/usr/bin/python
# coding: utf-8
#Author: Eitenne

import urllib
import sys
import json
from geopy.geocoders import Nominatim

if len(sys.argv) == 2:
	mac = sys.argv[1]
	geolocator = Nominatim()
	link = "http://api.mylnikov.org/geolocation/wifi?v=1.1&data=wpa2,wpa,wep,open&bssid=%s" % (mac)
	data = urllib.urlopen(link)
	content = data.read()
	obj = json.loads(content)
	lat = obj['data']['lat']
	long = obj['data']['lon']
        print "Lat: " + str(lat)
        print "Long" + str(long)
        place = str(lat) + "," + str(long)
        location = geolocator.reverse(place)
        print "Location: " + str(location)
else:
	print """Maclook v3.0( Eitenne )
Usage: maclook [BSSID]
     
EXAMPLES:
        python maclook.py 00:00:00:00
"""
