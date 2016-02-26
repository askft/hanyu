
import os
import sys

from prettytable import PrettyTable


COMMENT_IDENTIFIER = '#'
WORD_DELIMITER = '-'


def read(file):
	str = ""
	for line in file:
		if not (line.isspace() or (line.lstrip()[0] == COMMENT_IDENTIFIER)):
			str += line
	return str


def main(input):

	with open(input, 'r') as f:
		str = read(f)

	words = []

	lines = [line for line in str.splitlines() if line]

	for line in lines:
		ws = [s.strip() for s in line.split(WORD_DELIMITER)]
		if len(ws) != 3:
			print("Fail:")
			print(ws)
			print("Exiting.")
			exit(1)
		words.append(ws)

	t = PrettyTable(["English", "Pinyin", "汉语"])
	for l in words:
		print(l)
		t.add_row(l)
	print(t)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: python collect.py <input file>")
		exit(1)
	try:
		main(sys.argv[1])
	except:
		print("Unexpected error: %s" % sys.exc_info()[0])
		exit(1)

