#!/usr/local/bin/python
# reducer for lesson3 project part one
#
# Key is product category, value is total sales

import sys

oldKey = None
salesTotal = 0

# Loop over output of mapper
for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	# if something has gone wrong, skip this line
	if len(data_mapped) != 2:
		continue	
		
	thisKey, thisSale = data_mapped	

	if oldKey and oldKey != thisKey:
		print '{0}\t{1}'.format(oldKey, salesTotal)
		salesTotal = 0
	
	oldKey = thisKey
	salesTotal += float(thisSale)
	
# print the last output
if oldKey:
	print '{0}\t{1}'.format(oldKey, salesTotal)  		