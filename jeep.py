from __future__ import division 

from bs4 import BeautifulSoup

import re 

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
        eep_all_section = eebpage.find_all(id="clear-fix right-wide-column")
        #select the right element on the page
        #we want to select the clear-fix right-wide-column
        for li in eep_all_section:
            eep_id = li.find("div", class_="section")
            #Search in eep_id for whatever is in "strong" and make it a string
            #In EcoEvoPub entries it is "EcoEvoPub Series", for others it is the speaker's name
            eep_eep = eep_id.strong#.string()
            If eep_eep is None or eep_eep == 0 or eep_eep.string != "EcoEvoPub Series":
                break
            #If "EcoEvoPub Series" is found
            else:
                #if eep_eep == "EcoEvoPub Series":
                eep_id = li.find("div", class_="section")
                seminar_name = div.p
                if seminar_name is None or seminar_name == 0:
                    name = "no speaker"
                else: 
                    #find the name of the speaker(s)	
                    pattern = r"<p>([A-Za-z]* [A-Za-z]* ?[A-Za-z]?)<br/>" 
                    mm = re.search(pattern, str(eep_id), re.I)
                    name = mm.group(1)
                    #find date
                    pattern2 = r"<h4>(.* .* .*) </h4>"
                    mm2 = re.search(pattern2, str(eep_id), re.I)
                    date = mm2.group(1)
                    myfile.write(name)
                    myfile.write(', ')
                    myfile.write(date) 
                    myfile.write('\n')
                else: 
                    break
        #write name + ", " + date to the file
        
print "Done."
