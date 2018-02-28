import urllib

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

FILE_NAME = 'https://s3.amazonaws.com/tcmg476/http_access_log'

# Use open() to get a filehandle that can access the file
fh = urllib.urlopen(FILE_NAME)

# Loop through the file 
for line in fh:
	print(line)

