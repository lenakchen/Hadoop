#!/usr/local/bin/python
# reducer for lesson3 project part one
#
# Key is product category, value is sale amount
#
# Find the total sales value across all the stores, and the total number of sales. 
# Assume there is only one reducer.



import sys

totalSales = 0
numSales = 0

# Loop over output of mapper
for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	# if something has gone wrong, skip this line
	if len(data_mapped) != 2:
		continue	
		
	thisStore, thisSale = data_mapped	

	totalSales += float(thisSale)
	numSales += 1
	
# print the final result
print 'Total Sales\tTotal number of sales'
print '{0}\t{1}'.format(totalSales, numSales) 
	 		