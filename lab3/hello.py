#!/usr/bin/env python3
import cgi
import os
import cgitb
cgitb.enable()

print("Content-type: text/html")
print()
print("<meta charset=\"utf-8\">")
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print("</ul>")
