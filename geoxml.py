import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_281656.xml'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print data
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

print sum([int(c.text) for c in  tree.findall('.//comment/count')])

