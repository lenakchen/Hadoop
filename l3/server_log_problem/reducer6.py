#!/usr/local/bin/python
# reducer for lesson3 project part two
#
# Find the most popular file on the website: the file whose path occurs most often in access_log.
# Your reducer should output the file's path and the number of times it appears in the log.
# Key is web site path, value is 1. 

import sys

oldKey = None
totalHit = 0
popKey = None
popHit = 0

# Loop over output of mapper
for line in sys.stdin:
	data_mapped = line.strip().split()
	
	#print data_mapped, type(data_mapped), len(data_mapped)
	# if something has gone wrong, skip this line
	if len(data_mapped) != 1:
		continue	
		
	thisKey = data_mapped	

	if oldKey and oldKey != thisKey:
		if popHit < totalHit:
			popHit = totalHit
			popKey = oldKey
		totalHit = 0 
		
	oldKey = thisKey
	totalHit += 1
	
	
# print the result
if popKey:
	print 'most popular path\tnumber of appearance'
	print '{0}\t{1}'.format(popKey, popHit)  		