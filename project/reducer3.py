#!/usr/bin/env python

""" Final Project
Task Three: Top Tags
Write a mapreduce program that would output Top 10 tags, ordered by the number of 
questions they appear in.

For an extra challenge you can think about how to get a top 10 list of tags, where 
they are ordered by some weighted score of your choice. 

Please note that you should only look at tags appearing in questions themselves 
(i.e. nodes with node_type "question"), not on answers or comments.

Dataset: forum_node.tsv

The fields in forum_node that are the most relevant to the task are:
"id": id of the node
"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
"tagnames": space separated list of tags
"author_id": id of the author
"body": content of the post
"node_type": type of the node, either "question", "answer" or "comment"
"parent_id": node under which the post is located, will be empty for "questions"
"abs_parent_id": top node where the post is located
"added_at": date added

"""

import sys
import operator

oldTag = None
total_count = 0
top_10 = {}

def check_top_10():
	if len(top_10) == 10 and total_count > min(top_10.values()):			
		min_key = min(top_10, key=top_10.get)
		top_10.pop(min_key)
		top_10[oldTag] = total_count
	if len(top_10) < 10:
		top_10[oldTag] = total_count	

for line in sys.stdin:
	thisTag = line.strip()
	if oldTag and oldTag != thisTag:
		check_top_10()	
		total_count = 0
		
	oldTag = thisTag
	total_count += 1
		
if oldTag:
	check_top_10()			

top_10 = sorted(top_10.items(), key= lambda x: (-x[1], x[0]))

print 'Tag\tCounts'	
for tag in top_10:
	print '{0}\t{1}'.format(tag[0], tag[1])		