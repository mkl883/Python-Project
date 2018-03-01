import urllib
import re

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

FILE_NAME = 'https://s3.amazonaws.com/tcmg476/http_access_log'

# Use open() to get a filehandle that can access the file
fh = urllib.urlopen(FILE_NAME)
print "This will take a while to compute, please stand by until the program is finished..."

# Total requests 
print "Computing total requests..."
fj = urllib.urlopen(FILE_NAME)
total = 0
for line in fj:
	total += 1
print "The total amount of requests is %d" % (total)

# Requests per day
print "Computing requests per day and week..."
fk = urllib.urlopen(FILE_NAME)
tempday = "24/Oct/1994"
daytotal = 0
for line in fk:
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	parts = regex.split(line)
	partsnext = regex.split(fk.next())
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
print "Computing requests per month..."
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
		elif "Dec" in parts[1]:
			Dec +=1
		elif "Jan" in parts[1]:
			Jan +=1
		elif "Feb" in parts[1]:
			Feb +=1
		elif "Mar" in parts[1]:
			Mar +=1
		elif "Apr" in parts[1]:
			Apr +=1
		elif "May" in parts[1]:
			May +=1
		elif "Jun" in parts[1]:
			Jun +=1
		elif "Jul" in parts[1]:
			Jul +=1
		elif "Aug" in parts[1]:
			Aug +=1
		elif "Sep" in parts[1]:
			Sep +=1
print "Total requests for October are " + str(Oct)
print "Total requests for November are " + str(Nov)
print "Total requests for December are " + str(Dec)
print "Total requests for January are " + str(Jan)
print "Total requests for February are " + str(Feb)
print "Total requests for March are " + str(Mar)
print "Total requests for April are " + str(Apr)
print "Total requests for May are " + str(May)
print "Total requests for June are " + str(Jun)
print "Total requests for July are " + str(Jul)
print "Total requests for August are " + str(Aug)
print "Total requests for September are " + str(Sep)
			
