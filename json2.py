import json
import urllib


url= "http://python-data.dr-chuck.net/comments_281660.json  "
input = urllib.urlopen(url).read()

info = json.loads(input)
print sum([int(item['count']) for item in info['comments']])
  
