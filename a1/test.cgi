#!/usr/bin/python

import os, BeautifulSoup
CGIDATAPATH = "/u/kylbaker/cgi-pub/i211/a1/data"

print 'Content-type: text/html\n'

text = """
<html>
    <head><title>A1 example page</title></head>
    <body>
        <h3>Your table should look like this....</h3>
        ...but with the correct number of rows/columns, and proper image resizing.<br><br>
"""

lCurrentListDir = [f for f in os.listdir(CGIDATAPATH) if f[0] != '.']

myTot = len(lCurrentListDir)
myMod = 3
myDiv = 2 #number of images per row
myRem = myTot % myMod
#text +='<tt>['+str(lCurrentListDir)+'</tt>'
text +='<tt>['+"Images"+'</tt>'
text +='<table border="1">'
for i in range(len(lCurrentListDir)):
    text += "<tr>"
    for j in lCurrentListDir:
        text += "<td>"
        text += '<img src="./data/' + str(j) + '\" width=\"100%\""></td>'
    text += "</tr>"
text += """
        </table>
    </body>
</html>
"""
soup = BeautifulSoup.BeautifulSoup(text)
print soup.prettify()
