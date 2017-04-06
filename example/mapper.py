#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by tab

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace, then split the line into words by tab-delimited
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print "{0}\t{1}".format(store, cost)