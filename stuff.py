
import sys

from dictionary import *
from word import *


def main(input):

	DELIMITER = ";"
	d = Dictionary()

	with open(input, 'r') as file:

		for line in file:
			# TODO: Have functionality for organizing into categories here.
			w = Word(line, DELIMITER)
			d.add_word(w)

#	print("Printing all Word object in the Dictionary:")
#	for word in d.get_words():
#		print(word)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: python %s <input file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1])


