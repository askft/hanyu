
import os
import sys


IDENTIFIER_COMMENT	= ';'
IDENTIFIER_CATEGORY = '#'
WORD_DELIMITER		= '-'


def main(input, output):

	with open(input,  'r') as fin, \
		 open(output, 'w') as fout:

		def iscategory(line):
			"""Return true if line starts with IDENTIFIER_CATEGORY.
			"""
			return line.lstrip()[0] == IDENTIFIER_CATEGORY

		def iscomment(line):
			"""Return true if line starts with IDENTIFIER_COMMENT.
			"""
			return line.lstrip()[0] == IDENTIFIER_COMMENT

		def split(s):
			"""Split a string "x - y - z" into a list ['x','y','z'].
			"""
			return [w.strip() for w in s.split(WORD_DELIMITER)]

		# Skip irrelevant lines
		lines = [l for l in fin if not (l.isspace() or iscomment(l))]

		outlines = []
		for line in lines:
			if iscategory(line):
				category = ''.join(line.split(None, 1)[1]).rstrip()
				outlines.append(IDENTIFIER_CATEGORY + ' ' + category)
			else:
				try:
					(x, y, z) = split(line)
					outlines.append("%s ; %s ; %s" % (x, y, z))
				except ValueError:
					print("Invalid line in file %s: '%s'" % (input, line))
					exit(1)

		# Write the triples to a file in a format that is easy to parse.
		fout.write(os.linesep.join(outlines))


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: python %s <input file> <output file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1], sys.argv[2])

