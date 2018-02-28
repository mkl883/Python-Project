import urllib

link = urllib.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
lines = link.readlines()
for line in lines:
	print line
