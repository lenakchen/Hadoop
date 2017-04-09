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
lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line: 
"2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, use the date_added field and NOT the last_activity_at field.

Dataset: forum_node.tsv and forum_users.tsv 

The fields in forum_node that are the most relevant to the task are:
"id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	
"added_at"	

"5339"	"Whether pdf of Unit and Homework is available?"	"cs101 pdf"	"100000458"	""	
"question"	"\N"	"\N"	"2012-02-25 08:09:06.787181+00"	

forum_users contains: "user_ptr_id"	"reputation"	"gold"	"silver"	"bronze"
"""

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if line[3] == "author_id":
		continue
	author_id = line[3]
	added_at = line[8]
	hour = datetime.strptime(added_at[:-3], "%Y-%m-%d %H:%M:%S.%f").hour
	print "{0}\t{1}".format(author_id, hour)
	
    
