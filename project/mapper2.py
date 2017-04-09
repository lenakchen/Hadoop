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
import csv
#import re

reader = csv.reader(sys.stdin, delimiter='\t')
   
for line in reader:
	# find the node id of a forum post
    node_id = line[0]
    if node_id == 'id':
    	continue
    body = line[4]	
    node_type = line[5]
    ##remove html tags
    #tags = re.compile('<.*?>')
    #body = re.sub(tags, '', body)
    post_len = len(body)
    if node_type == 'question':
    	print '{0}\t{1}\t{2}'.format(node_id, 'A', post_len)
    if node_type == 'answer':
    	abs_parent_id = line[7]
    	print '{0}\t{1}\t{2}'.format(abs_parent_id, 'B', post_len)
    	
    
    
    