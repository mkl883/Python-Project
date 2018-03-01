import urllib
import re

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

FILE_NAME = 'https://s3.amazonaws.com/tcmg476/http_access_log'

# Use open() to get a filehandle that can access the file
fh = urllib.urlopen(FILE_NAME)
print "This will take a while to compute, please stand by..."

Oct, Nov, Dec, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep = 0,0,0,0,0,0,0,0,0,0,0,0
for line in fh:
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	parts = regex.split(line)
	partsnext = regex.split(fh.next())
	if len(partsnext) < 7 or len(parts)<7:
		temp = 9
	else:
		if "Oct" in parts[1]:
			Oct += 1
		elif "Nov" in parts[1]:
			Nov +=1
		elif "Nov" in parts[1]:
			Dec +=1
		elif "Nov" in parts[1]:
			Jan +=1
		elif "Nov" in parts[1]:
			Feb +=1
		elif "Nov" in parts[1]:
			Mar +=1
		elif "Nov" in parts[1]:
			Apr +=1
		elif "Nov" in parts[1]:
			May +=1
		elif "Nov" in parts[1]:
			Jun +=1
		elif "Nov" in parts[1]:
			Jul +=1
		elif "Nov" in parts[1]:
			Aug +=1
		elif "Nov" in parts[1]:
			Sep +=1
			

# Total requests 
total = 0
for line in fh:
	total += 1
print "The total amount of requests is %d" % (total)

# Requests per day
tempday = "24/Oct/1994"
daytotal = 0
for line in fh:
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	parts = regex.split(line)
	partsnext = regex.split(fh.next())
	if len(partsnext) < 7 or len(parts)<7:
		temp = 9
	else:
		if parts[1] == tempday:
			daytotal += 1
		else:
			print ("Total number of requests for " + parts[1] + " is " + str(daytotal))
			daytotal = 0
			tempday = partsnext[1]

# Requests per month
