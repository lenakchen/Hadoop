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
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	tagnames = line[2].strip()
	if tagnames == 'tagnames':
		continue
	node_type = line[5].strip()	
	if node_type == 'question':	
		tagnames = tagnames.split()
		for tag in tagnames:
			print tag
		
	