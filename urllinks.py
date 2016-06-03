# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Reily.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
i=6
l =[re.findall('by_(.+)\.',url)[0]]
while i>=0:
    
    tags = soup('a')
    tag = tags[17]
    l.append(str(tag.contents[0]))
    link = str(tag.get('href', None))
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    i-=1
print l