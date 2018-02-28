import urllib
import re

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

FILE_NAME = 'https://s3.amazonaws.com/tcmg476/http_access_log'

# Use open() to get a filehandle that can access the file
fh = urllib.urlopen(FILE_NAME)
print "This will take a while to compute, please stand by..."
# Loop through the file 
total = 0
for line in fh:
	total += 1
print "The total amount of requests is %d" % (total)

	
	


