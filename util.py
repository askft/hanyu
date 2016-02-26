

IDENTIFIER_COMMENT  = ';'
IDENTIFIER_CATEGORY = '#'

DELIMITER_NUM       = '-'		# TODO Change this to something else (?)
DELIMITER_NICE      = ' | '		# Note the spaces

NUM_LANGUAGES       = 3


def iscategory(line):
	"""Return true if line starts with IDENTIFIER_CATEGORY.
	"""
	return line.lstrip()[0] == IDENTIFIER_CATEGORY


def iscomment(line):
	"""Return true if line starts with IDENTIFIER_COMMENT.
	"""
	return line.lstrip()[0] == IDENTIFIER_COMMENT


def split(s, delimiter):
	"""Split a string "x DELIMITER_NUM y DELIMITER_NUM z"
	into a list ['x','y','z'].
	"""
	return [w.strip() for w in s.split(delimiter)]

