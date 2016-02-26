
import sys

from dictionary import *
from word       import *
from util       import *


def create_dictionary_from_file(file):

	categeory           = 'CATEGORY_MISSING'
	d                   = Dictionary()

	for line in file:
		if line[0] == IDENTIFIER_CATEGORY:
			category = line[1:].strip()
			d.add_category(category)
		else:
			w = Word(line, DELIMITER_NICE)
			w.add_category(category)
			d.add_word(w)

	return d


def main(input):
	with open(input, 'r') as file:
		d = create_dictionary_from_file(file)

# ----- Tests ------------------------------------------------------------------

	print("Printing all Word object in the Dictionary:")
	for word in d.get_words():
		print(word)
	print()
	
	print("Printing all pronouns:")
	for word in d.get_words_for_category("Pronouns"):
		print(word)
	print()

	print("Printing all categories in the dictionary:")
	for category in d.get_categories():
		print("- %s" % category)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: python %s <input file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1])


