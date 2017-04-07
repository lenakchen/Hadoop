#!/usr/bin/env python
# mapper for lesson3 project part two
#
# Format of each line in access_log is in Common Log Format:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# %h %l %u %t \"%r\" %>s %b
# IP address 
# identity of the client
# username of the client 
# time [day/month/year:hour:minute:second zone]
# request line from the client: method, path, query-string, and protocol or the request
# status code that the server sends back to the client: 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found)
# size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
#
# Find the most popular file on the website: the file whose path occurs most often in access_log.
# Your reducer should output the file's path and the number of times it appears in the log.
# IMPORTANT: Some pathnames in the log begin with 'http://www.the-associates.co.uk'.
# Be sure to remove the portion from pathnames in your mapper so that all occurrences of a file are counted together.
#
 

import sys

for line in sys.stdin:
	data = line.strip().split()
	#print data, type(data), len(data)
	if len(data) == 10:
		ip, id, username, datetime, timezone, method, path, protocol, status, size = data
		print path.replace('http://www.the-associates.co.uk', '')
		