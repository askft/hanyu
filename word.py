
from util import *

class Word:
	"""A Word is a collection of synonyms in different languages.
	"""

	def __init__(self, str, delimiter):
		self.categories = []
		self.delimiter = delimiter

		langs     = split(str, delimiter)
		self.list = [split(lang, ',') for lang in langs]

#		print("Added definition:", self.list)

	def add_category(self, category):
		self.categories.append(category)

	def __str__(self):
#		inner = ['[' + ', '.join(['\'' + s + '\'' for s in lang]) + ']' \
#			for lang in self.list]
#		outer = ', '.join(inner)
#		return '[' + outer + ']'
		inner = [', '.join([s for s in lang]) for lang in self.list]
		outer = ' | '.join(inner)
		cats = ', '.join(self.categories)
		return '< Word: { ' + outer + ' } ( ' + cats + ' ) >'
	
