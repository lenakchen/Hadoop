#!/usr/local/bin/python
# reducer for lesson3 project part two
#
# task1: Write a MapReduce program which will display the number of hits for each different file on the Web site.
# task2: Write a MapReduce program which determines the number of hits to the site made by each different IP address.  
# Key is web site path (task 1) or ip address (task 2), value is 1. 

import sys

oldKey = None
totalHit = 0

# Loop over output of mapper
for line in sys.stdin:
	data_mapped = line.strip().split()
	
	#print data_mapped, type(data_mapped), len(data_mapped)
	# if something has gone wrong, skip this line
	if len(data_mapped) != 1:
		continue	
		
	thisKey = data_mapped	

	if oldKey and oldKey != thisKey:
		print '{0}\t{1}'.format(oldKey, totalHit)
		totalHit = 0
	
	oldKey = thisKey
	totalHit += 1
	
# print the last output
if oldKey:
	print '{0}\t{1}'.format(oldKey, totalHit)  		