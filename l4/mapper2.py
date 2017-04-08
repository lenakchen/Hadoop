#!/usr/bin/env python

# Format of each line in purchases.txt is
# data\ttime\tstore\tproduct category\tcost\tpayment method
#
# Write a mapreduce program that processes the purchases.txt file and outputs mean of sales
# for each weekday.

import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) == 6:
		date, time, store, product, cost, payment = data
		# get the weekday
		weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
		print '{0}\t{1}'.format(weekday, cost)
