#!/usr/bin/env python

# Format of each line in purchases.txt is
# data\ttime\tstore\tproduct category\tcost\tpayment method
#
# Write a mapreduce program that processes the purchases.txt file and outputs mean of sales
# for each weekday.

import sys

oldKey = None
sumSale = 0
count = 0

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) != 2:
		continue
	thisKey, thisSale = data_mapped
	if oldKey and oldKey != thisKey:
		print '{0}\t{1}'.format(oldKey, sumSale/count)
		count = 0
		sumSale = 0
		
	oldKey = thisKey
	sumSale += float(thisSale)
	count += 1	

if oldKey:
	print '{0}\t{1}'.format(oldKey, sumSale/count)
		