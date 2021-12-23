# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, 
# read the XML data from that URL using urllib and then parse and extract 
# the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter - ')
html=urllib.request.urlopen(url, context=ctx).read()
print('Retrieving: ' + url)
print('Retrieved',len(html), 'characters')

tree=ET.fromstring(html)
counts = tree.findall('.//count')
sum=0
ct=0

for item in counts:
    cc=int(item.text)
    ct+=1
    sum+=cc

print('Count:',ct)
print('Sum:',sum)
