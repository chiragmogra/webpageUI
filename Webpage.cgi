#! /usr/bin/python3

import cgi
import cgitb   #cgitb --> cgi traceback to see error in the browser instead of going to os for troubleshoot
import subprocess

#to show common error in webbrowser
cgitb.enable()

print("Content-type:text/html")
print("")

webdata=cgi.FieldStorage() #this is collect all the html code with data
#now extracting value of x
data = webdata.getvalue('x')
#sending output of client via web server
op=subprocess.getoutput(data)
print("<pre>")
print(op)
print("</pre>")
