#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import urllib2
from BeautifulSoup import BeautifulSoup

version = "v2.0"
author = "Eitenne"

def main():
     if len(sys.argv) == 2:
          url = sys.argv[1]
          soup = BeautifulSoup(urllib2.urlopen(url))
          title = soup.title.string
          print "[*] Downloading..."
          print "[*] Title:", title
          print "[*] Url:", url
          os.system("wget http://www.youtubeinmp3.com/fetch/?video=" + url + " -O '" + title + ".mp3' &> /dev/null")
          print "[!] Done, file saved as %s.mp3" % (title)
     else:
          print """Ytdl """ + version + """( https://kssec.ga )
Usage: ytdl [youtube-url] [Options]
     
EXAMPLES:
         python ytdl.py https://www.youtube.com/watch?v=UMNtZBTXbmQ
INFO:
     format : .mp3
     Author : """ + author + """
     Api    : http://www.youtubeinmp3.com/
          """


main()
