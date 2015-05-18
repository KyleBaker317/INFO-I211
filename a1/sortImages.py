#!/usr/bin/python
# # # # # # # # # # # # # # # #
# File: sortImages.py         #
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
import os
import time
from PIL import Image
from PIL.ExifTags import TAGS

def returnImageList():
	directory = "/u/kylbaker/cgi-pub/i211/a1/data"
	p=os.listdir(directory)
	#print p
	p.sort(key=lambda x: os.stat(os.path.join(directory, x)).st_mtime)
#	sortedList = []
#	for file in p:
#		f = file.split(".")
#		if f[len(f)-1] == "bmp":
#			fileName = f[0]
#			new = time.strptime(fileName,"%Y%m%d%H%M%S")
#			sortedList.append(new)
#	sortedList.sort()
#	newList= []
#	for item in sortedList:
#		item = time.strftime("%Y%m%d%H%M%S",item)
#		item = item+".bmp"
#		newList.append(item)
	#print "Old List: ",p
	#print "New List: ", p
	return p
def get_exif_data(fname):
	directory = "/u/kylbaker/cgi-pub/i211/a1/data"
	exifData = {}
	text = ""
	imgPath = os.path.join(directory, fname)
	try:
		img = Image.open(imgPath)
		try:
			exifinfo = img._getexif()
			if exifinfo != None:
				for tag, value in exifinfo.items():
					decoded = TAGS.get(tag, tag)
					exifData[decoded] = value
			for element in ["Date Time", "Exif Version", "Model"]:
				textCompressed = element.replace(" ","")
				text += element + ":" + str(exifData[textCompressed]) +"<BR>"
		except:
			text += "Datatype Not Supporeted<BR>Cannot Provide Exif Data for BMP files"
	except:
		text += "File is not an Image"
	return text
if __name__ ==	"__main__":
	#returnImageList()
	get_exif_data("20140408122732.bmp")