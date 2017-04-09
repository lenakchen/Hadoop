#!/usr/bin/env python
# Combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data
"""
The goal is to have the output from the reducer with the following fields for each forum post: 
"id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at" 
"score"  "reputation"  "gold"  "silver"  "bronze"
"""

import sys
user = {}
post = {}

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	# data mapped from forum_users input
	if len(data_mapped) == 6 and data[1] == 'A':
		user_id, input, reputation, gold, silver, bronze = data_mapped		
		user[user_id] = [reputation, gold, silver, bronze]
	# data mapped from forum_node input
	if len(data_mapped) == 10 and data[1] == 'B':
		author_id, input, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data_mapped
		post[author_id] = [id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score]

for key in post.keys():
	print '\t'.join(post[key]),'\t','\t'.join(user[key])
		
		
#user = {'sape': ['0', '12'], 'jack': ['88', '99'], 'guido': ['27', '34']}		
#tel = {'sape': ['413', '9', '1', '2', '3'], 'jack': ['40', '98', '6', '33', '10'], 'guido': ['41', '27', '34', '1', '0']}

#for key in tel.keys():
#	print '\t'.join(tel[key]),'\t','\t'.join(user[key])