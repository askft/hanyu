
import os
import sys

from prettytable import *


COMMENT_IDENTIFIER	= '#'
WORD_DELIMITER		= '-'


def table(list, header):
	"""Return a new PrettyTable created from `list` and `header`.
	"""
	t = PrettyTable(header)
	for element in list:
		t.add_row(element)
	t.align = 'l'
#	t.set_style(PLAIN_COLUMNS)
	return t


def main(input, output):

	with open(input, 'r') as file:

		def iscomment(line):
			return line.lstrip()[0] == COMMENT_IDENTIFIER

		def ok(line):
			return not (line.isspace() or iscomment(line))

		def split(s):
			"""Split a string "x - y - z" into a list ['x','y','z'].
			"""
			return [w.strip() for w in s.split(WORD_DELIMITER)]

		# A triple is something like ['big', 'dà', '大'].
		# `triples` is a list of such.
		triples = [split(line) for line in file if ok(line)]

	# Detect incomplete triples.
	if not all([len(t) == 3 for t in triples]):
		print("Length error.")
		exit(1)

	# Print a nice table. Unnecessary but fun.
#	print(table(triples, ["English", "Pinyin", "汉语"]))

	# Write the triples to a file in a format that is easy to parse.
	with open(output, 'w') as file:
		for [a, b, c] in triples:
			file.write("%s ; %s ; %s" % (a, b, c))
			file.write(os.linesep)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: python collect.py <input file> <output file>")
		exit(1)
	main(sys.argv[1], sys.argv[2])

