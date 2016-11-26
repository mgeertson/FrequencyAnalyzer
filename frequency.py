#!/usr/bin/python

import sys
import collections

message = sys.argv[1]

letters = collections.Counter(message)
del letters[' ']

print("\n************************************")
print("Printing letters and their frequency")
print("************************************\n")

for pair in letters:
	print(pair,letters[pair])

	
