# IMPORTANT
# Before running make sure to delete old versions of save files or else the information will be added again

import urllib
import re
from collections import Counter

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

# Requests per day and week
print "Computing requests per day and week..."
fk = urllib.urlopen(FILE_NAME)
tempday = "24/Oct/1994"
daytotal = 0
counter = 0
weektotal = 0
for line in fk:
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	parts = regex.split(line)
	partsnext = regex.split(fk.next())
	if len(partsnext) < 7 or len(parts)<7:
		temp = 9
	else:
		if parts[1] == tempday:
			daytotal += 1
			if counter < 7:
				weektotal += 1
			else:
				print ("Total requests for this week is " + str(weektotal))
				counter = 0
				weektotal = 0
		else:
			print ("Total number of requests for " + parts[1] + " is " + str(daytotal))
			daytotal = 0
			counter += 1
			tempday = partsnext[1]

# Requests per month, also saves in files by month
print "Computing requests per month and saving to text files..."
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
			with open('october.txt', 'a') as octfile:
				octfile.write(line)
		elif "Nov" in parts[1]:
			Nov +=1
			with open('november.txt', 'a') as novfile:
				novfile.write(line)
		elif "Dec" in parts[1]:
			Dec +=1
			with open('december.txt', 'a') as decfile:
				decfile.write(line)
		elif "Jan" in parts[1]:
			Jan +=1
			with open('january.txt', 'a') as janfile:
				janfile.write(line)
		elif "Feb" in parts[1]:
			Feb +=1
			with open('february.txt', 'a') as febfile:
				febfile.write(line)
		elif "Mar" in parts[1]:
			Mar +=1
			with open('march.txt', 'a') as marfile:
				marfile.write(line)
		elif "Apr" in parts[1]:
			Apr +=1
			with open('april.txt', 'a') as aprfile:
				aprfile.write(line)
		elif "May" in parts[1]:
			May +=1
			with open('may.txt', 'a') as mayfile:
				mayfile.write(line)
		elif "Jun" in parts[1]:
			Jun +=1
			with open('june.txt', 'a') as junfile:
				junfile.write(line)
		elif "Jul" in parts[1]:
			Jul +=1
			with open('july.txt', 'a') as julfile:
				julfile.write(line)
		elif "Aug" in parts[1]:
			Aug +=1
			with open('august.txt', 'a') as augfile:
				augfile.write(line)
		elif "Sep" in parts[1]:
			Sep +=1
			with open('september.txt', 'a') as sepfile:
				sepfile.write(line)
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

# Unsuccessful requests
print "Computing unsuccessful requests (4xx)..."
fm = urllib.urlopen(FILE_NAME)
totalu = 0
for line in fm:
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	parts = regex.split(line)
	if len(parts) < 7:
		temp = 0
	elif "4" == parts[6][0]:
		totalu += 1
print "The total amount of unsuccessful requests is %d" % (totalu)
percentu = (float(totalu))/(float(total)) * 100
print "The percentage of unsucessful requests is " + str(percentu) + "%"

# Redirected requests
print "Computing redirected requests (3xx)..."
fn = urllib.urlopen(FILE_NAME)
totalr = 0
for line in fn:
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	parts = regex.split(line)
	if len(parts) < 7:
		temp = 0	
	elif "3" == parts[6][0]:
		totalr += 1
print "The total amount of redirected requests is %d" % (totalr)
percentr = (float(totalr))/(float(total)) * 100
print "The percentage of redirected requests is " + str(percentr) + "%"

# Most requested file and least requested
print "Computing most requested and 10 least requested files..."
f0 = urllib.urlopen(FILE_NAME)
totalr = 0
templist = []
for line in f0:
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	parts = regex.split(line)
	if len(parts) < 7:
		temp = 0	
	else:
		templist.append(parts[4])
c = Counter(templist)
print ("The most requested file is " + str(c.most_common(1)))
print ("Ten of the least requested files are " + str(c.most_common()[:-11:-1]))
