
class Word:
	"""A Word is a collection of synonyms in different languages.
	"""

	def __init__(self, str, delimiter):
		self.categories = []
		self.delimiter = delimiter

		langs     = [s.strip() for s in str.split(delimiter)]
		self.list = [[s.strip() for s in lang.split(',')] for lang in langs]

#		print("Added definition:", self.list)

	def add_category(self, category):
		self.categories.append(category)

	def __str__(self):
#		inner = ['[' + ', '.join([s for s in lang]) + ']' for lang in self.list]
#		outer = ', '.join(inner)
#		return '[' + outer + ']'
		inner = [', '.join([s for s in lang]) for lang in self.list]
		outer = ' | '.join(inner)
		return '<Word: { ' + outer + ' }>'
	
