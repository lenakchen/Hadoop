#!/usr/bin/env python

# Format of each line in purchases.txt is
# data\ttime\tstore\tproduct category\tcost\tpayment method
#
# Write a mapreduce program that processes the purchases.txt file and outputs mean of sales
# for each weekday.
# Use reducer as combiner too in this process.

import sys

import sys

oldKey = None
allSales = []

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) != 2:
		continue
	thisKey, thisSale = data_mapped
	if oldKey and oldKey != thisKey:
		print '{0}\t{1}'.format(oldKey, sum(allSales)/len(allSales))
		allSales = []
		
	oldKey = thisKey
	allSales.append(float(thisSale))

if oldKey:
	print '{0}\t{1}'.format(oldKey, sum(allSales)/len(allSales))
		