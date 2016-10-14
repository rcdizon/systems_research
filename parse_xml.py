#!/usr/bin/env python

import sys
#from bs4 import BeautifulSoup

#soup = BeautifulSoup(open(sys.argv[1]), 'lxml')
#model_location = lambda x: x.name == "Model"
#model = soup(model_location)
#print(model)

def get_name(line):
    beg_index = line.index("name=\"")  + 6
    end_index = line.index("\"", beg_index)
    name = "Name:" + line[beg_index : end_index]
    return name

def get_xmi_type(line):
    beg_index = line.index("xmi:type=\"")  + 14
    end_index = line.index("\"", beg_index)
    typ = line[beg_index : end_index]
    return typ

f = open('output.txt', 'r')
for line in f:
    if "<packagedElem" in line: 
        information = ""

        if "uml:Class" in line:
            uml_type = "UML:Class"
            name = get_name(line)
            owned_attributes = []
            next_line = next(f) 
            while not "</packagedElem" in next_line:
                if "<ownedAttr" in next_line:
                    owned_attributes.append(get_xmi_type(next_line) + "," + get_name(next_line))
                next_line = next(f)
            print name, uml_type, "Contains:", owned_attributes

        elif "uml:InformationFlow" in line:
            source = ""
            target = ""
            uml_type = "UML:InformationFlow"
            name = get_name(line)
            print name, uml_type

        elif "uml:Property" in line:
            uml_type = "UML:Property"
            name = get_name(line)
            print name, uml_type

        elif "uml:Association" in line:
            member_end = ""
            print "Found an association!"

        elif "uml:Port:" in line:
            uml_type = "UML:Port"
            name = get_name(line)
            print name, uml_type
        
        #print information
f.close()
