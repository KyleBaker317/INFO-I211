#!/usr/bin/python
# # # # # # # # # # # # # # # #
# PART C                      #
# File: index.cgi             #
# --------------------------- #
# Team Number: 15             #
# Kyle Baker [ Creator ]      #
# Gabe McHaley                #
# Erika Finkle                #
# Michael Schulenburg         #
# --------------------------- #
# Partner Team Number: 16     #
# Adam Neel                   #
# Connor Hartzog              #
# John Kurtis Waldon          #
# Zachary Michael Ruland      #
# --------------------------- #
# Created: 4/8/2014           #
# Last Edited: 4/6/2014       #
# Last Edited by: Kyle Baker  #
# # # # # # # # # # # # # # # #


# Sets location for modules to be imported from
# import sys; sys.path.append("/u/kylbaker/pythonModules") 
# Allows browser to display errors from python script
import cgitb; cgitb.enable() 
import os, BeautifulSoup, wrapper
import sortImages
from PIL import Image
from PIL.ExifTags import TAGS
CGIDATAPATH = "/u/kylbaker/cgi-pub/i211/a1/data"

sortedImageList = sortImages.returnImageList()
# Text to eventually write to the page
text = ""
# total number of images to be written
myTot = len(sortedImageList)
# number of images per row
myDiv = 3 
# number of columns
myRem = myTot / myDiv 
# opens the table tag
text += '<table class="textWithBorder" border="0">'
# loops through the number of columns
for i in range(myRem):
    text += "<tr>"  # opens the table row
    for j in range(myDiv):
        currentImage = str(sortedImageList[j + myDiv * i])
        caption = sortImages.get_exif_data(currentImage)
        text += "<td>"  # opens the table element
        text += '<img class=\"image\" src="./data/' + currentImage + '\" width=\"100%\"">'
        text += "<h2>" +caption + "</h2>"
        text += '</td>'  # closes the table element
    text += "</tr>"  # closes the table row
text += "</table>"  # closes the table

# wraps the text in the HTML wrapper defined in wrapper Module
wrapper.wrapHTML(text, "Assignment 1")
