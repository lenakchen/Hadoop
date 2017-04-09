#!/usr/bin/env python
""" Final Project
Task One: Students and Posting Time on Forums

Find for each student what is the hour during which the student has posted the most posts. 
Output from reducers should be:
author_id    hour
For example:
13431511\t13
54525254141\t21
If there is a tie: there are multiple hours during which a student has posted a maximum 
number of posts, print the student-hour pairs on separate lines. The order in which these 
lines appear in output does not matter.

Ignore the time-zone offset for all times - for example in the following line: 
"2012-02-25 08:11:01.623548+00" - Ignore the +00 offset.
"""
### Updated version of reducer.py. Avoid using long lists and dictionary.

import sys
from collections import Counter

oldKey = None
all_hours = [0]*24


for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) != 2:
		continue
	thisKey, thisHour = data_mapped	
	if oldKey and oldKey != thisKey:
		max_num = max(all_hours)		
		for hour, count in enumerate(all_hours):
			if count == max_num:
				print '{0}\t{1}'.format(oldKey, hour)
		all_hours = [0]*24	
		
	oldKey = thisKey
	all_hours[int(thisHour)] += 1
	
# output the last result
if oldKey:
	max_num = max(all_hours)		
	for hour, count in enumerate(all_hours):
		if count == max_num:
			print '{0}\t{1}'.format(oldKey, hour)
		
		