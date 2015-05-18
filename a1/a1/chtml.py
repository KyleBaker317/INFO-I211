#!/usr/bin/python
# File = chtml.py
# I211 Spring 2014 - Lecture 15
# your name (Baker, Kyle)
# kylbaker
# 15
# Erika Finkle | Michael Schulenburg | Gabe McHaley
import os, sys, random
import cgitb; cgitb.enable()
from BeautifulSoup import BeautifulSoup
main = __name__ == "__main__"
def createPages():
	""" Creates pages from files that end in .page """
	files = os.listdir(os.curdir)
	for file in files:
		fileList = file.split(".")
		x = len(fileList)-1
		extension = fileList[x]
		title = fileList[0]
		#print "\nName: ",file
		#print "Length:",str(len(fileList))
		#print "Extension:",str(extension)
		if extension == "page":
			newTitle = title+".cgi"
			
			newPage = '''#!/usr/bin/python
import chtml
import cgitb
cgitb.enable()
from BeautifulSoup import BeautifulSoup
chtml.wrapPage("'''+file+"\")"
			#print type(newPage)
			#print "Exists?", os.path.isfile(newTitle)
			if not os.path.isfile(newTitle):
				#print "hello"
				f = open(newTitle, 'w+')
				f.write(newPage)
				f.close()
				os.chmod(newTitle,0755)

def header(title=sys.argv[0]):
	if (title==sys.argv[0]):
		title=title.split(".")
		title=title[0]
	print """Content-type: text/html\n\n
	<html>
		<head><title>%s</title></head>
	<body>
	""" % title
def extensionList():
	file = os.listdir(os.curdir)
	allExtensions = []
	for f in file:
		f = f.split(".")
		if len(f) == 1:
			extension = "DIRECTORY"
		else:
			extension= f[len(f)-1]
		if extension not in allExtensions:
			allExtensions.append(extension)
		#print extension
	return allExtensions

def createLink(fi, title="NONE"):
	if title=="NONE":
		title = fi
	return "<a href=\""+fi+"\">" +title+"</a>"

def createULfromExtensions():
	files = os.listdir(os.curdir)
	extensions = extensionList()
	#print extensions
	lsTP={} #dictionary
	imgExt=["png","jpg"]
	for ext in extensions:
		lsTP[ext]= []
	for f in files:
		fileName = f
		f = f.split(".")
		if len(f) == 1:
			extension = "DIRECTORY"
		else:
			extension= f[len(f)-1]
		lsTP[extension].append(fileName)
		
	return lsTP
def footer():
	print """
		</body>
	</html>
	"""

## MAIN


def createMenu():
	["Directories","Images","Programming Files","Other"]
	dir = createULfromExtensions2()
	menuTabs = ["Directories","Images","Programming Files","Other"]
	if main: print dir
	#	dontIndex=["css","pyc","html~","py~","cgi~","cgi#","py#","bak"]
	#	extensions = extensionList()
	#	extensions = sorted(extensions)
	#	if "page"  in extensions:
	#		extensions.remove("page")
	#		newExtensions=["page"]
	#		for item in extensions:
	#			newExtensions.append(item)
	#		extensions= newExtensions
	string = ""
	string += "<ul>\n"
	for key in menuTabs:
		tabName = key
		tabFiles = dir[key]
		tabFiles = sorted(tabFiles, key=lambda v: v.upper())# sorts list with  no regard to Capititalization
		#print "key: %s , value: %s" % (tabName, tabFiles)
		string += '<li><a class="top"><span>{tabName}</span></a>\n<ul>'.format(tabName=tabName)
		for f in tabFiles:
			name = f.split(".")
			name = name[0]
		#print f
			string += '<li><a href="'+str(f)+'">'+str(f)+'</a></li>\n'
		string += '</ul>\n'	
	#soup = BeautifulSoup(string)
	#return soup.prettify()
	return string
def fileToHTML(file):
	""" Encodes a page in text that can be rendered by html documenting"""
	ls= open(file,"r").readlines() #list containing content of
	allowed= "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,\
	u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,\
	T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9, "
	allowed=allowed.split(",")
	final = ""
	for string in ls:
		string=string.decode("utf-8")
		#return "STRING: ",string
		for character in string:
			#return "Character: ", character
			if character == "\t":
				final = final+"<&nbsp&;nbsp&;nbsp&;nbsp;>"
			elif character == ("\n" or "\r"):
				final= final +"<BR>"
				#print "NLC"
			elif character in allowed:
				final= final+character
				#print "Allowed"
			else:
				decimalCode=ord(character)
				hecCode=hex(decimalCode)[2:]
				#print hecCode
				final+= "&#x"+hecCode+";"
	return final
def titleCreate(title):
	title = title.split(".")[0]
	string = ""
	seperators = "-,.,_"
	for character in title:
		if character in seperators:
			string += " "
		else:
			string += character
	return string

def wrapPage(page, type="none"):
	"""wrapPage(page, type) | type is optional"""
	# Setting Variables
	menu = createMenu()
	style = '''<link href="indexFiles/style_home.css" rel="stylesheet" type="text/css" />
	  <link href="indexFiles/menu.css" rel="stylesheet" type="text/css" />'''
	title = titleCreate(page)
	mainContent = ""
	if type == "none":
		mainContent = fileToHTML(page)
	elif type == "pdf":
		mainContent='''<object	data="'''+page+'''#toolbar=1&amp;navpanes=0&amp;scrollbar=1&amp;page=1&amp;view=FitH" 
		type="application/pdf" 
		width="100%" 
		height="1000px">'''
	else:
		str = ""
		f = open(page,"r").readlines()
		for line in f:
			str+= line
		mainContent = str
	menu = createMenu()
	print 'Content-type: text/html\n\n'
	content = '''<!DOCTYPE html>
	<html>
	 <head>
	  <title>
	{title}
	  </title>
	  {style}
	 </head>
	 <body>
	  <div class="wrapper">
	   <div class="titlebar">
		<center>
		 <div class="title">{title}
		 </div><!-- title -->
		</center>
	   </div> <!-- titlebar -->
	   <div id="menu">
		<div class="left">
		</div><!-- left -->
		<div class="right">
		</div><!-- rigtt -->
		<div class="center">{menu}</div>
	   </div><!-- menu -->
	   <div class="content_front_page">
		<p>{main}</p>
	   </div> <!-- content_front_page -->
	  </div><!-- wrapper -->
	  <div class="push">
	  </div> <!-- push -->
	 </body>
	</html>
	'''.format(title=title,style=style,menu=menu,main = mainContent)
	soup = BeautifulSoup(content)
	print soup.prettify()

def randomColor():
	red=hex(random.randrange(51)*5)
	green=hex(random.randrange(51)*5)
	blue=hex(random.randrange(51)*5)
	
	newcolor= str(red)[2:]+str(green)[2:]+str(blue)[2:]
	return  newcolor
def wrapPage2(page, type="none"):
	

	newColor = randomColor()
	# Setting Variables
	menu = createMenu()
	title = titleCreate(page)
	style = """<link href="indexFiles2/style.css" rel="stylesheet" type="text/css" />
	  <link href="indexFiles2/menu.css" rel="stylesheet" type="text/css" />
	  <link href="indexFiles2/fonts.css" rel="stylesheet" type="text/css" /><style>
	#menu .center {{
	background-color: #{color};
	}}
        #menu .center ul li {{
	background-color: #{color};
        }}
	</style>""".format(color = newColor)
	
	mainContent = ""
	if type == "none":
		mainContent = fileToHTML(page)
	elif type == "pdf":
		mainContent='''<object	data="'''+page+'''#toolbar=1&amp;navpanes=0&amp;scrollbar=1&amp;page=1&amp;view=FitH" 
				type="application/pdf" 
				width="100%" 
				height="1000px">'''
	else:
		str = ""
		f = open(page,"r").readlines()
		for line in f:
			str+= line
		mainContent = str
	#!!!!!!!
	print 'Content-type: text/html\n\n'
	page = '''
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	 <head>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	  <title>
	   {title}
	  </title>{style}
	 </head>
	 <body>
	  <div class="all">
	   <div class="header">
		{title}
	   </div>
	   <!--header-->
	   
	   <div id="menu">
		<div class="center">
		 {menu}
		</div>
		<!-- center -->
	   </div>
	   <!-- menu -->
	   
	   <div class="main">
		{main}
	   </div>
	   <!--main-->
	  </div>
	  <!--all-->
	 </body>
	</html>
	'''.format(title= title,style=style, menu=menu, main = mainContent)
	soup = BeautifulSoup(page)
	#print page
	print soup.prettify()


def testMenu():
	# List of tab title and the extensions that are included in the tab.
	# format is a list of a list containing a string and a list of file extensions
	# NOTE: folders are given the extension "DIRECTORY" (files that have no extension)
      	# Example of acceptable format:
	# [["Programming Files",["cgi","py","py~"]],["Directories",["DIRECTORY"]]]
	tabs = [["Programming Files",["cgi","py","py~"]],["Directories",["DIRECTORY"]]]
	print "Starting Test Menu Function"
	files = os.listdir(os.curdir)
	for tab in tabs:
		print tab[0] #Executes function on the tab name e.g "Programming Files"
		for extension in tab[1]:
			print "\t",extension # executes function on extension in tab name e.g "cgi"
def printContentsOfDirectory():
	for file in files:
		print "File: ",
		print file
		fileNameSplit = file.split(".")
		lengthOfFile =  len(fileNameSplit)
		if lengthOfFile == 1: #checks to see if the file is a Directory
			extension = "dir"
		else:
			extension = fileNameSplit[lengthOfFile-1]
		print "Extension: ",extension,"\n"
def createULfromExtensions2():
	files = os.listdir(os.curdir)
	files = sorted(files, key=lambda v: v.upper())# sorts list with  no regard to Capititalization	
	#for file in files:
	#	print file
	extensions = extensionList()
	tabs = [["Images",["png","jpg"]],["Programming Files",["cgi","py","py~"]],["Directories",["DIRECTORY"]]]
	lsTP={} #dictionary
	indexed = []
	lsTP["Other"]= []
	for tab in tabs:
		tabTitle = tab[0]
		lsTP[tabTitle]= []
	for f in files:
		fileName = f
		f = f.split(".")
		extension = ""
		fileLen = len(f)
		if len(f) == 1:
			extension = "DIRECTORY"
		else:
			extension= f[len(f)-1]
		for tab in tabs:
			if extension in tab[1]:
				lsTP[tab[0]].append(fileName)
				indexed.append(fileName)
				break
		if fileName not in indexed:
			if main: print fileName
			lsTP["Other"].append(fileName)	
	return lsTP



if __name__ == "__main__":
	#createPages()
	#print createMenu()
	#testMenu()
#	files = os.listdir(os.curdir)
#	files = sorted(files, key=lambda v: v.upper())# sorts list with  no regard to Capititalization	
#	for file in files:
#		print file
#	dict = createULfromExtensions2()
#	for key in dict.keys():
#		tabName = key
#		tabFiles = dict[key]
#		tabFiles = sorted(tabFiles, key=lambda v: v.upper())# sorts list with  no regard to Capititalization	
#		print tabName
#		for file in tabFiles:
#			print "\t",file
	#print fileToHTML("lorem-ipsum-utf8.page")
	print randomColor()

