#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

from dictionary import *
from word       import *
from util       import *


def create_dictionary_from_file(file):

	first_line = file.readline()
	languages  = split(first_line[1:].strip(), ',')
	d          = Dictionary(languages)

	category = 'CATEGORY_MISSING'

	for line in file:

		if line.isspace():
			continue

		if line[0] == IDENTIFIER_CATEGORY:
			category = line[1:].strip()
			d.add_category(category)
		else:
			list = [split(lang, ',') for lang in split(line, DELIMITER_NICE)]
			w = Word(list)
			w.add_category(category)
			d.add_word(w)

	return d


def choose_languages(available_languages):

	print("Avaliable languages are:")
	i = 1
	for lang in available_languages:
		print(" - [%d] %s" % (i, lang))
		i += 1

	print()

	(lang_from, lang_to) = (None, None)

	while True:
		try:
			lang_from = int(input("Select language to translate from: ")) - 1
			if lang_from not in range(len(available_languages)):
				raise ValueError

			lang_to = int(input("Select language to translate to: ")) - 1
			if lang_to not in range(len(available_languages)):
				raise ValueError

		except (ValueError, IndexError):
			print("Invalid input. Please try again.\n")

		else:
			break

	print()

	return (lang_from, lang_to)


def choose_categories(available_categories):

	print("Available categories are:")
	i = 1
	for category in available_categories:
		print(" - [%d] %s" % (i, category))
		i += 1

	print()

	chosen_categories = None
	while True:
		try:
			user_input = input(
					"Enter categories to include words from.\n"
					"Separate choices by whitespace.\n"
					"Enter nothing to include all categories.\n"
					"Input: ")

			choices = [int(x.strip()) for x in user_input.split()]

			chosen_categories = \
				[available_categories[choice - 1] for choice in choices]

			if not chosen_categories:
				chosen_categories = available_categories

		except (ValueError, IndexError):
			print("Invalid input. Please try again.\n")

		else:
			break

	return chosen_categories


# TODO
#  Fix for unanswered words and ?exit exiting if incorrect_words is empty

def practice(lang_from, lang_to, words):

	num_correct      = 0
	num_incorrect    = 0

	correct    = []
	incorrect  = []
	unanswered = list(words)

	for word in words:

		challenge = ', '.join(word.list[lang_from])
		answer = split(input("Translate '%s': " % challenge), ',')

		if ''.join(answer) == '?exit':
			print()
			break

		for a in answer:

			a = convert_to_acc(a) 

			if a in word.list[lang_to]:
				num_correct += 1
				correct.append(word)
				print(GREEN + "'" + a + "' is correct. Good!\n" + ENDC)
				break

			else:
				num_incorrect += 1
				s = ' | '.join([', '.join(x) for x in word.list])
				incorrect.append(word)
				print(RED + "Bad! Correct answer: ( %s ).\n" % (s) + ENDC)
				break

		unanswered.remove(word)

	return (num_correct, num_incorrect, correct, incorrect, unanswered)


def main(input_filename):
	with open(input_filename, 'r') as file:
		d = create_dictionary_from_file(file)

	print("\n   --- 学汉语 ---\n")

	(lang_from, lang_to) = choose_languages(d.get_languages())
	chosen_categories    = choose_categories(d.get_categories())

	words = list(d.get_words_for_categories(chosen_categories))

	num_correct   = 0
	num_incorrect = 0

	try_again = True
	while try_again:

		random.shuffle(words)

		(new_num_correct, new_num_incorrect, correct, incorrect, unanswered) = \
			practice(lang_from, lang_to, words)

		num_correct   += new_num_correct
		num_incorrect += new_num_incorrect

		ratio = num_correct / (num_correct + num_incorrect)

		total = len(correct) + len(incorrect) + len(unanswered)
		print(
			"%sCorrect:%s    %d of %d\n"
			"%sIncorrect:%s  %d of %d\n"
			"%sUnanswered:%s %d of %d\n" % (
				GREEN,  ENDC, len(correct),    total,
				RED,    ENDC, len(incorrect),  total,
				YELLOW, ENDC, len(unanswered), total))


#		print("You got " + YELLOW + ("%.2f %%" % (ratio * 100.0)) + ENDC + \
#				" of the words " + GREEN + "correct.\n" + ENDC)

		if not incorrect and not unanswered:
			print("Congratulations!\n")
			break

		print(GREEN + "The following words were correct:" + ENDC)
		for word in correct:
			s = ' | '.join([', '.join(x) for x in word.list])
			print(" - %s" % s)
		print()

		print(RED + "The following words were incorrect:" + ENDC)
		for word in incorrect:
			s = ' | '.join([', '.join(x) for x in word.list])
			print(" - %s" % s)
		print()

		print(YELLOW + "The following words were left unanswered:" + ENDC)
		for word in unanswered:
			s = ' | '.join([', '.join(x) for x in word.list])
			print(" - %s" % s)
		print()

		while True:
			choice = input(
					"Try again with the incorrect and unanswered words? [y/n] ")
			if choice == 'y':
				words = incorrect + unanswered
				break
			elif choice == 'n':
				print("Thank you for using the program.")
				try_again = False
				break
			else:
				print("Invalid input. Please try again.")


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: python %s <input file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1])


