#!/usr/local/bin/python
# mapper for lesson3 project part one
#
# Format of each line in purchases.txt is
# data\ttime\tstore\tproduct category\tcost\tpayment method
#
# Give a sales breakdown by product category across all of our stores.
# Find the monetary value for the highest individual sale for each separate store.
# Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

import sys

for line in sys.stdin:
	
	data = line.strip().split('\t')
	
	if len(data) == 6:
		date, time, store, product, cost, payment = data
		print '{0}\t{1}'.format(product, cost)


		