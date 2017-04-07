#!/usr/local/bin/python
# reducer for lesson3 project part one
#
# Key is product category, value is sale amount
#
# Break the sales down by product category across all of the stores.


import sys

oldProduct = None
salesTotal = 0

# Loop over output of mapper
for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	# if something has gone wrong, skip this line
	if len(data_mapped) != 2:
		continue	
		
	thisProduct, thisSale = data_mapped	

	if oldProduct and oldProduct != thisProduct:
		print '{0}\t{1}'.format(oldProduct, salesTotal)
		salesTotal = 0
	
	oldProduct = thisProduct
	salesTotal += float(thisSale)
	
# print the last output
if oldProduct:
	print '{0}\t{1}'.format(oldProduct, salesTotal)  		