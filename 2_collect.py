#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys

from util import *


def main(input, output):

	with io.open(input,  'r', encoding='utf-8') as fin:

		outlines = []

		for line in fin:

			# Skip irrelevant lines
			if line.isspace() or iscomment(line):
				continue

			if islanguage(line):
				languages = ''.join(line.split(None, 1)[1]).rstrip()
#				print("languages = %s" % languages)
				outlines.append(IDENTIFIER_LANGUAGE + ' ' + languages)

			elif iscategory(line):
				category = ''.join(line.split(None, 1)[1]).rstrip()
#				print("category = %s" % category)
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

	with io.open(output, 'w', encoding='utf-8') as fout:
		fout.write(os.linesep.join(outlines))


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: python %s <input file> <output file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1], sys.argv[2])

