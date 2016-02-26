
class Dictionary:
	"""A Dictionary is a list of Word objects.
	"""

	def __init__(self):
		self.words = []

	def add_word(self, word):
		self.words.append(word)

	def get_words(self):
		return self.words

	def get_words_for_category(self, category):
		return [word for word in self.words if category in word.categories]

