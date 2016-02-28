#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

from dictionary import *
from word       import *
from util       import *


DEBUG = False


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
	print(
		"Enter categories to include words from.\n"
		"Separate choices by whitespace.\n"
		"Enter nothing to include all categories.\n")
	while True:
		try:
			user_input = input("Choose category: ")

			choices = [int(x.strip()) for x in user_input.split()]

			chosen_categories = \
				[available_categories[choice - 1] for choice in choices]

			if not chosen_categories:
				chosen_categories = available_categories

		except (ValueError, IndexError):
			print("Invalid input. Please try again.\n")

		else:
			break
	print()

	return chosen_categories


def practice(lang_from, lang_to, correct, incorrect, unanswered):

	# Note on the shuffle: the + function returns a copy.
	words = incorrect + unanswered
	random.shuffle(words)
	for word in words:

		challenge = ', '.join(word.list[lang_from])
		answer = split(input("Translate '%s': " % challenge), ',')

		if ''.join(answer) == '?exit':
			print()
			break

		for a in answer:

			a = convert_to_acc(a) 

			# Correct answer
			if a in word.list[lang_to]:

				if word in unanswered:
					unanswered.remove(word)
					if DEBUG: print("Removed %s from unanswered" % word)

				if word in incorrect:
					incorrect.remove(word)
					if DEBUG: print("Removed %s from incorrect" % word)

				# Is this check necessary? (If not, just append the word).
				if word not in correct:
					correct.append(word)
					if DEBUG: print("Added %s to correct" % word)
				else:
					if DEBUG: print("The correct check is necessary!")

				print(GREEN + "'" + a + "' is correct. Good!\n" + ENDC)
				break

			# Incorrect answer
			else:
				s = ' | '.join([', '.join(x) for x in word.list])

				if word in unanswered:
					if DEBUG: print("Removed %s from unanswered" % word)
					unanswered.remove(word)

				# Is this check necessary? (If not, just append the word).
				if word not in incorrect:
					incorrect.append(word)
					if DEBUG: print("Added %s to incorrect" % word)
				else:
					if DEBUG: print("The incorrect check is necessary!")

				print(RED + "Bad! Correct answer: ( %s ).\n" % (s) + ENDC)
				break


def main(input_filename):

	# Read categories and words from file and load into a dictionary
	with open(input_filename, 'r', encoding='utf-8') as file:
		d = create_dictionary_from_file(file)

	print("\n   --- 学汉语 ---\n")

	(lang_from, lang_to) = choose_languages(d.get_languages())
	chosen_categories    = choose_categories(d.get_categories())

	words = list(d.get_words_for_categories(chosen_categories))

	correct    = []
	incorrect  = []
	unanswered = list(words)

	random.shuffle(unanswered)

	try_again = True
	while try_again:

		practice(lang_from, lang_to, correct, incorrect, unanswered)

		if not incorrect and not unanswered:
			print("Congratulations! You got all of the words right.\n")
			break

		total = len(correct) + len(incorrect) + len(unanswered)
		print(
			"%sCorrect:%s    %d of %d\n"
			"%sIncorrect:%s  %d of %d\n"
			"%sUnanswered:%s %d of %d\n" % (
				GREEN,  ENDC, len(correct),    total,
				RED,    ENDC, len(incorrect),  total,
				YELLOW, ENDC, len(unanswered), total))

		while True:
			choice = input("Show remaining words? [y/n] ")
			if choice == 'y':
				def show(list, color, name):
					if not list:
						return
					print(color + "The following words were %s:" % name + ENDC)
					list.sort(key=lambda w: w.list[0][0], reverse=True)
					for word in list:
						s = ' | '.join([', '.join(x) for x in word.list])
						print(" - %s" % s)
				show(correct,    GREEN,  "correct")
				show(incorrect,  RED,    "incorrect")
				show(unanswered, YELLOW, "unanswered")
				break
			elif choice == 'n':
				break
			else:
				print("Invalid input. Please try again.\n")
		print()

		while True:
			remaining = ""
			if incorrect and not unanswered:
				remaining = "incorrect"
			elif unanswered and not incorrect:
				remaining = "unanswered"
			elif incorrect and unanswered:
				remaining = "incorrect and unanswered"
			else:
				break
			# (The lists will never both be empty at the same time because of
			# the break a few blocks up ("all words were answered correctly").
			# Hence we don't actually need an else statement.)
			choice = input("Try again with the %s words? [y/n] " % remaining)
			if choice == 'y':
				break
			elif choice == 'n':
				print("Thank you for using the program.")
				try_again = False
				break
			else:
				print("Invalid input. Please try again.\n")
		print()


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: python %s <input file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1])

