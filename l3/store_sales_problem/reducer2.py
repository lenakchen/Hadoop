#!/usr/local/bin/python
# reducer for lesson3 project part one
#
# Key is store name, value is sale amount
# Find the monetary value for the highest individual sale for each separate store.

import sys

oldStore = None
maxSale = 0

# Loop over output of mapper
for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	# if something has gone wrong, skip this line
	if len(data_mapped) != 2:
		continue	
		
	thisStore,thisSale = data_mapped	

	if oldStore and oldStore != thisStore:
		print '{0}\t{1}'.format(oldStore, maxSale)
		maxSale = 0	
	
	oldStore = thisStore
	maxSale = max(float(thisSale), float(maxSale))
	
# print the last output
if oldStore:
	print '{0}\t{1}'.format(oldStore, maxSale)  		