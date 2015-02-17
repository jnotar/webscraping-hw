#!/usr/bin/python

from __future__ import division 

from bs4 import BeautifulSoup

import re 

#these might be important packages
import os  
import pdb
from codecs import open

with open("eep_speakers.txt", "w", "utf-8") as myfile:
    myfile.write("Name")
    myfile.write(", ")
    myfile.write("Date")
    myfile.write('\n')
    for i in range(1,800): #Iterate for all 800 pages
        #turn i into a filename that open() can read
        file = str(i) + ".html"
        #parse each file into a tree structure
        eebpage = BeautifulSoup(open(file)) #parse each file into a tree structure
        #find the right section of the webpage
        eep_pane = eebpage.find(id="main-content")
        #select the right element on the page
        #we want to select the clear-fix right-wide-column
        eep_id = eep_pane.find("div", class_="clear-fix right-wide-column")
        #Search in eep_id for whatever is in "strong" and make it a string
        #In EcoEvoPub entries it is "EcoEvoPub Series", for others it is the speaker's name
        eep_eep = eep_id.strong#.string
        #If "EcoEvoPub Series" is found
        if eep_eep == "EcoEvoPub Series":
            #find the name of the speaker(s)	
            pattern = r"<p>([A-Za-z]* [A-Za-z]* ?[A-Za-z]?)<br/>" 
            mm = re.search(pattern, str(eep_id), re.I)
            name = mm.group(1)
            #find date
            pattern2 = r"<h4>(.* .* .*) </h4>"
            mm2 = re.search(pattern2, str(eep_id), re.I)
            date = mm2.group(1)
        else: 
            break
        #write name + ", " + date to the file
        myfile.write(name)
        myfile.write(", ")
        myfile.write(date) 
        myfile.write('\n')
print "Done"
