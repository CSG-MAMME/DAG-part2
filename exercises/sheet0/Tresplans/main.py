#!/usr/bin/env python3

import sys
import time

def compare_pair(b1, b2, bases):
	"""
	Compare two bases and return True or False.
	Return True if there exists both B1 \ {x} U {y} and B2 \ {y} U {x}.
	Return False otherwise.
	"""
	# Get x and y using bit substraction.
	x = b1 & ~b2
	y = b2 & ~b1

	# For all bits in x.
	for i in range(len(bin(x)[2:])):
		# If there is no 1 in the i-th bit of x.
		if not 1 << i & x:
			# Go to next bit of x.
			continue
		match = False
		# For all bits in y
		for j in range(len(bin(y)[2:])):
			# If there is no 1 in the j-th bit of y.
			if not 1 << j & y:
				# Go to next bit of y.
				continue
			# B1 \ {x} U {y}
			if bases.get(b1 & ~(1 << i) | (1 << j), False):
				match = True
				break
		# If there was no match, return False.
		if not match:
			return False
	return True


def compare_bases(bases):
	"""
	Traverse a dictionary with bases and return True or False.
	Return True if the set of bases create a matroid.
	Return False otherwise.
	"""
	# Get all the keys (bases) into a list.
	# Useful to data type to avoid comparing the same bases twice.
	# Traverse the list of bases until the next-to-last base.
	# Assign the base to b1.
	for b1 in bases.keys():
		# Travserse the list again from the base next to b1 to the last one.
		# Assign the base to b2.
		for b2 in bases.keys():
			if b1 == b2:
				continue
			# Compare every pair of bases.
			# The function compare_pair compares both
			# B1 \ {x} U {y} and B2 \ {y} U {x}.
			if not compare_pair(b1, b2, bases):
				return False

	return True


def process_file(f):
	# Create a dictionary.
	bases = {}
	# Traverse all lines of the file.
	for line in f:
		# Start a "hash" variable.
		h = 0 
		# Ignore lines starting with '#' character.
		if line[0] is '#':
			continue
		# Split lines into integers (x).
		# Sum to the "hash" variable a bit shifted by x bits.
		for x in line.split():
			h |= 1 << int(x)
		# Create a dictionary entry with the "hash" variable.
		bases[h] = 1

	return bases

# Execute only if file is called directly
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage:   " + str(sys.argv[0]) + "FILE(S)")
		print("Example: " + str(sys.argv[0]) + "../matroid-or-not/*.bases")
		sys.exit(1)

	# Get all the supplied files.
	files = sys.argv[1:]
	
	# Variable only to pretty print output.
	file_max_length = max([len(x) for x in files])

	# Do for all files.
	for current_file in files:
		t_start = time.time() # Start timer
		# Open a file.
		with open(current_file) as f:
			# Process the file and construct a dictionary.
			bases = process_file(f)
			# Print if the file contains the bases of a matroid or not.
			if len(bases) and compare_bases(bases):
				print(current_file.rjust(file_max_length) + " -> Matroid.")
			else:
				print(current_file.rjust(file_max_length) + " -> No matroid")

		t_end = time.time() # End timer
		print(str(t_end - t_start) + " seconds")

	sys.exit(0)
