#!/usr/bin/env python

# Richard Dizon
# parse_xml.py
# 10/14/16

import sys

def get_name(line):
    beg_index = line.index("name=\"")  + 6
    end_index = line.index("\"", beg_index)
    name = "Name:" + line[beg_index : end_index]
    return name

def get_xmi_type(line):
    beg_index = line.index("xmi:type=\"")  + 14 # Must account for leading type info
    end_index = line.index("\"", beg_index)
    typ = line[beg_index : end_index]
    return typ

object_dict = {}

def get_xmi_id(line):
    beg_index = line.index("xmi:idref=\"") + 11
    end_index = line.index("\"", beg_index)
    xmi_id = line[beg_index : end_index]
    return xmi_id

def add_object(line, name):
    global object_dict
    beg_index = line.index("xmi:id=\"") + 8
    end_index = line.index("\"", beg_index)
    obj_entry = line[beg_index : end_index]
    object_dict[obj_entry] = name

used_object_dict = {}

def used_add_object(line, name):
    global used_object_dict
    beg_index = line.index("xmi:id=\"") + 8
    end_index = line.index("\"", beg_index)
    obj_entry = line[beg_index : end_index]
    used_object_dict[obj_entry] = name

def get_href(line):
    beg_index = line.index("href=\"") + 7 # Must account for leading ref characters
    end_index = line.index("\"", beg_index)
    xmi_id = line[beg_index : end_index]
    return xmi_id

f = open('output.txt', 'r')
for line in f:
    if "<packagedElem" in line: 

        if "uml:Class" in line:
            uml_type = "UML:Class"
            name = get_name(line)
            owned_attributes = []
            next_line = next(f) 
            while not "</packagedElem" in next_line:
                if "<ownedAttr" in next_line:
                    owned_attributes.append(get_xmi_type(next_line) + "," + get_name(next_line))
                    add_object(next_line, name)
                #if "<usedObjects" in next_line:
                    #add_object(line, name)
                next_line = next(f)
            print name, uml_type, "Contains:", owned_attributes

        elif "uml:InformationFlow" in line:
            source = "Source:"
            target = "Target:"
            uml_type = "UML:InformationFlow"
            name = get_name(line)
            next_line = next(f)
            while not "</packagedElem" in next_line:
                if "<informationSource" in next_line:
                    source += (object_dict[get_xmi_id(next_line)])
                if "<informationTarget" in next_line:
                    target += (object_dict[get_xmi_id(next_line)])
                next_line = next(f)

            print name, uml_type, source, target

        elif "uml:Property" in line:
            uml_type = "UML:Property"
            print uml_type

        elif "uml:Association" in line:
            uml_type = "UML:Association"
            print uml_type

        elif "uml:Port:" in line:
            uml_type = "UML:Port"
            name = get_name(line)
            print name, uml_type
        
f.close()

f = open('output.txt', 'r')
for line in f:
   if "xmi:id=\"" in line and "uml:Property" in line:
        name = "umi:Property"
        used_add_object(line, name)        
   if "xmi:id=\"" in line and "uml:Association" in line:
        name = "umi:Association"
        used_add_object(line, name)        
   if "xmi:id=\"" in line and "name=\"" in line:
        name = get_name(line)
        used_add_object(line, name)        
f.close()

f = open('output.txt', 'r')
print "\nUsed objects:"
for line in f:
   if "<usedObjects" in line:
        print used_object_dict[get_href(line)]
f.close()
