#!/usr/bin/python
# # # # # # # # # # # # # # # #
# File: wrapper.cgi           #
# Kyle Baker's Page Template  #
# Created: 4/6/2014           #
# Last Edited: 4/6/2014       #
# Last Edited by: Kyle Baker  #
# # # # # # # # # # # # # # # #

# Sets location for modules to be imported from
import sys; sys.path.append("/u/kylbaker/pythonModules") 
# Allows browser to display errors from python script
import cgitb; cgitb.enable() 
import chtml

from BeautifulSoup import BeautifulSoup
"""Module to wrap different file formats in certain HTML wrap"""
main = __name__ == "__main__"
def wrapHTML(html="", title= "Default Title"):
    # Setting Variables
    newColor = chtml.randomHTMLColor() 
    menu = chtml.createMenu()
    title = chtml.titleCreate(title)
    style = """<link href="http://cgi.soic.indiana.edu/~kylbaker/indexFiles2/style.css" rel="stylesheet" type="text/css" />
      <link href="http://cgi.soic.indiana.edu/~kylbaker/indexFiles2/menu.css" rel="stylesheet" type="text/css" />
      <link href="http://cgi.soic.indiana.edu/~kylbaker/indexFiles2/fonts.css" rel="stylesheet" type="text/css" /><style>
    #menu .center {{
    background-color: {color};
    }}
        #menu .center ul li {{
    background-color: {color};
        }}
    </style>""".format(color = newColor)
    page = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
     <!-- # # # # # # # # # # # # # # # # -->
     <!-- # File: movefile.cgi          # -->
     <!-- # --------------------------- # -->
     <!-- # Team Number: 15             # -->
     <!-- # Kyle Baker [ Creator ]      # -->
     <!-- # Gabe McHaley                # -->
     <!-- # Erika Finkle                # -->
     <!-- # Michael Schulenburg         # -->
     <!-- # --------------------------- # -->
     <!-- # Partner Team Number: 16     # -->
     <!-- # Adam Neel                   # -->
     <!-- # Connor Hartzog              # -->
     <!-- # John Kurtis Waldon          # -->
     <!-- # Zachary Michael Ruland      # -->
     <!-- # --------------------------- # -->
     <!-- # Created: 4/8/2014           # -->
     <!-- # Last Edited: 4/6/2014       # -->
     <!-- # Last Edited by: Kyle Baker  # -->
     <!-- # # # # # # # # # # # # # # # # -->
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
    '''.format(title= title,style=style, menu=menu, main = html)
    print 'Content-type: text/html\n\n'
    soup = BeautifulSoup(page)
    print soup.prettify()

def wrapHTML2(html, title= "Default Title"):
    """wrapPage(page, type) | type is optional"""
    # Setting Variables
    page = html
    menu = chtml.createMenu()
    style = '''<link href="http://cgi.soic.indiana.edu/~kylbaker/indexFiles/style_home.css" rel="stylesheet" type="text/css" />
      <link href="http://cgi.soic.indiana.edu/~kylbaker/indexFiles/menu.css" rel="stylesheet" type="text/css" />'''
    title = chtml.titleCreate(page)
    mainContent = ""
    menu = chtml.createMenu()
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

############ END OF MODULE ##############
if main:
    print "Main Statement"
    wrapHTML("HELLO")
    newColor = chtml.randomHTMLColor()
    print newColor