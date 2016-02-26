
import os
import sys

from util import *


def main(input, output):

	with open(input,  'r') as fin, \
		 open(output, 'w') as fout:

		# Skip irrelevant lines
		lines = [l for l in fin if not (l.isspace() or iscomment(l))]

		outlines = []

		for line in lines:

			if iscategory(line):
				category = ''.join(line.split(None, 1)[1]).rstrip()
				outlines.append(IDENTIFIER_CATEGORY + ' ' + category)

			else:
				tokens = split(line, DELIMITER_NUM)
				if len(tokens) != NUM_LANGUAGES:
					print("Invalid line in file %s: '%s'" % (input, line))
					exit(1)

				outline = ""
				for i in range(len(tokens)):
					if i == 0: outline +=                  tokens[i]
					else:      outline += DELIMITER_NICE + tokens[i]

				outlines.append(outline)

		# Write the triples to a file in a format that is easy to parse.
		fout.write(os.linesep.join(outlines))


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: python %s <input file> <output file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1], sys.argv[2])

