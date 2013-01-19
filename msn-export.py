import sys
from xml.dom.minidom import parse
 
if len(sys.argv) != 2:
	sys.stderr.write("usage: " + sys.argv[0] + " <inputfile>")
	sys.exit(1)
 
doml = parse(sys.argv[1])
for message in doml.getElementsByTagName("Message"):
	user = (message.getElementsByTagName("From")[0]
	              .getElementsByTagName("User")[0])
	date = message.getAttribute('Date')
	time = message.getAttribute('Time')
	name = "%s %s %s says" % (date, time, user.getAttribute("FriendlyName")) + " says:"
	print name.encode('utf-8')
	msg = message.getElementsByTagName("Text")[0].firstChild.nodeValue
	print msg.encode('utf-8')
	print