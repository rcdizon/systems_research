#!/usr/bin/env python

import sys
#from bs4 import BeautifulSoup

#soup = BeautifulSoup(open(sys.argv[1]), 'lxml')
#model_location = lambda x: x.name == "Model"
#model = soup(model_location)
#print(model)


f = open('output.txt', 'r')
for line in f:
    if "<packagedElem" in line: 
        if "uml:Class" in line:
            name = ""
            owned_attributes = []
            print "Found a class!"
        elif "uml:InformationFlow" in line:
            name = ""
            source = ""
            target = ""
            print "Found InFlow!"
        elif "uml:Property" in line:
            name = ""
            print "Found a property!"
        elif "uml:Association" in line:
            member_end = ""
            print "Found an association!"
        elif "uml:Port:" in line:
            name = ""
            print "Found a port!"
f.close()
