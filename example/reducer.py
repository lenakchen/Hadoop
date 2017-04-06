#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
#
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
    # parse the input we got from mapper.py
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
    	# Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

	# this IF-switch only works because Hadoop sorts map output
    # by key (here: thisKey) before it is passed to the reducer
    if oldKey and oldKey != thisKey:
    	# write result to STDOUT
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

# output the last key
if oldKey != None:
    print oldKey, "\t", salesTotal