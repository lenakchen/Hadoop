#!/usr/bin/env python

# Create an index of all words that can be found in the body of a forum post 
# and node id they can be found in
# Do not parse the HTML. Just split the text on all whitespace as well as the following
# characters: .,!?:;"()<>[]#$=-/
# Quiz:
# How many times was the word 'fantastic' used on forums?
# List of comma separated nodes the word 'fantastically' can be found in :

# Format of each line in forum_node.tsv is: 
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	
# "added_at"	"score"	"state_string"	"last_edited_id"	"last_activity_by_id"	
# "last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"	"extra_count"	"marked"
# The above is the first line. Not every item has value. It may be "" or "\N"
# "5339"	"Whether pdf of Unit and Homework is available?"	"cs101 pdf"	"100000458"	""	
# "question"	"\N"	"\N"	"2012-02-25 08:09:06.787181+00"	"1"	""	"\N"	"100000921"	
# "2012-02-25 08:11:01.623548+00"	"6922"	"\N"	"\N"	"204"	"f"
#
# Format of each line in forum_users.tsv is: 
# "user_ptr_id"	"reputation"	"gold"	"silver"	"bronze"
#


import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
   
for line in reader:
	#print line
	# find the node id of a forum post
    node_id = line[0].strip()
    if node_id == 'id':
    	continue
    # find the body of a post and converts all cased characters to lowercase	
    body = line[4].strip()
    
    #remove html tags
	#tags = re.compile('<.*?>')
 	#body = re.sub(tags, '', body)
 	 
    # split the text on all whitespace and punctuation
    words = re.findall(r"[\w']+", body.lower())
    for w in words:
    	print '{0}\t{1}'.format(w, node_id)
    	

# alternative split
# word=re.split(r"[*+%.!?,:;\"()<>\[\]#$=\-\/\s]", body.lower())