from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

FILE_NAME = 'https://s3.amazonaws.com/tcmg476/http_access_log'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

# Loop through the file 
for line in fh:
	print(line)


# The loop example above is memory-efficient, and also easy to read