import urllib
import sys

def urlencode(raw):
	print urllib.quote(raw)

def urldecode(encoded):
	print urllib.unquote(encoded);

def __exit__():
	print "read the fucking source code"
	exit()

cmds = {
	'urlencode':urlencode,
	'urldecode':urldecode
}


if not len(sys.argv) == 3:
	__exit__()

cmd = sys.argv[1]
arg = sys.argv[2]

if not cmds.has_key(cmd):
	__exit__()

cmds[cmd](arg)
