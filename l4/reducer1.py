#!/usr/bin/env python

# Create an index of all words that can be found in the body of a forum post 
# and node id they can be found in
# Quiz:
# How many times was the word 'fantastic' used on forums?
# List of comma separated nodes the word 'fantastically' can be found in :

import sys

old_word = None
wordcount = 0
word_index = 1
old_node = []

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped) != 2:
		continue
	
	this_word, this_node = data_mapped
	
	if old_word and old_word != this_word:
		# sort the node id in ascending order
		old_node.sort()
		# print the list of nodes separated by comma
		print '{0}\t{1}\t{2}\t{3}'.format(word_index, old_word, wordcount, ', '.join(old_node))
		word_index += 1
		wordcount = 0
		old_node = []
		
	old_word = this_word
	wordcount += 1
	old_node.append(this_node)

if old_word:
	old_node.sort()
	print '{0}\t{1}\t{2}\t{3}'.format(word_index, old_word, wordcount, ', '.join(old_node))
	
			