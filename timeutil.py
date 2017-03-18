import time
import sys

def getCurrentTimestamp():
	nowInMills = (int) (time.time() * 1000)
	print nowInMills

def getCurrentTime():
	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) 

def getTimestampFor(stringTime):
	print (int) (time.mktime(time.strptime(stringTime, "%Y-%m-%d %H:%M:%S")) * 1000)

def getTimeFor(timestamp):
	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp) / 1000)) 

def getHelp():
	print "read the fucking source code"

def __exit__():
	switch['h']()
	exit()

switch = {
	'cs':getCurrentTimestamp,
	'ct':getCurrentTime,
	's':getTimestampFor,
	't':getTimeFor,
	'h':getHelp
}

#for line in hongbaoyu:
#	getTimestampFor(line)

#getCurrentTimestamp()

cmdLength = len(sys.argv)
if cmdLength < 2:
	__exit__()

cmd = sys.argv[1]

if not switch.has_key(cmd):
	__exit__()

if cmdLength == 2:
	switch[cmd]()

if cmdLength == 3:
	arg = sys.argv[2]
	switch[cmd](arg)
