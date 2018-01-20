#!/usr/bin/python

import requests
import sys
import os
import json

from lxml.html import fromstring
from terminaltables import AsciiTable

if len(sys.argv) == 3:
	range_lol = sys.argv[2]
	for x in range(int(range_lol)):
		target = "%s/?author=%s" % (sys.argv[1],x) 
		r = requests.get(target)
		tree = fromstring(r.content)
		title = tree.findtext('.//title')
		titre = title.split(',')[0]
		if titre.startswith('Page'):
			continue
		else:
			print "[*] USER: %s" % (titre)
else:
	print "./%s <url> <range>" % (sys.argv[0])
