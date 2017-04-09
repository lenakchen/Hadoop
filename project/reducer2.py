#!/usr/bin/env python
""" Final Project
Task Two: Post and Answer Length
Find if there is a correlation between the length of a post and the length of answers.

Write a mapreduce program that would process the forum_node data and output the length
of the post and the average answer (just answer, not comment) length for each post.

Dataset: forum_node.tsv

The fields in forum_node that are the most relevant to the task are:
"id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	

"""

import sys

oldID = None
total_answer_length = 0
count = 0

print 'Question Node ID\t|Question Length\t|Average Answer Length'	
for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) != 3:
		continue
	node_id, node_type, post_length = data_mapped
	
	if oldID and oldID != node_id:
		if total_answer_length > 0:
			answer_length = total_answer_length/count
		else:
			answer_length = 0		
		print '{0}\t{1}\t{2}'.format(oldID, question_length, answer_length)
		total_answer_length = 0
		count = 0
				
	oldID = node_id
	# if node type is question
	if node_type == 'A':
		question_length = post_length
	# if node type is answer
	if node_type == 'B':
		total_answer_length += float(post_length)
		count += 1	
	
if oldID:
	if total_answer_length > 0:
		answer_length = total_answer_length/count
	else:
		answer_length = 0
	print '{0}\t{1}\t{2}'.format(oldID, question_length, answer_length)
		
	