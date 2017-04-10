#!/usr/bin/env python

""" Final Project
Task Four: Study Groups
Write a mapreduce program that for each forum thread (that is a question node with all
it's answers and comments). This would give us a list of students that have posted there -
either asked the question, answered a question or added a comment. If a student posted to
that thread several times, they should be added to that list several times as well, to
indicate intensity of communication.

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
	# student ID is "author_id" from forum_nodes file. 
	node_id = line[0].strip()
	if node_id == 'id':
		continue
	author_id = line[3].strip()
	node_type = line[5].strip()
	if node_type == 'question':
		print '{0}\t{1}'.format(node_id, author_id)
	if node_type == 'answer' or node_type == 'comment':
		abs_parent_id = line[7].strip()
		print '{0}\t{1}'.format(abs_parent_id, author_id)	
		
	