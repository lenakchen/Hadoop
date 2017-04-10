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
oldNode = None
studentList = []

print 'Question Node ID |Student IDs'

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) != 2:
		continue
	thisNode, thisStudent = data_mapped
	if oldNode and oldNode != thisNode:		
		print '{0}\t{1}'.format(oldNode, ', '.join(studentList))
		studentList = []

	oldNode = thisNode
	studentList.append(thisStudent)

if oldNode:		
	print '{0}\t{1}'.format(oldNode, ', '.join(studentList))
