
# Convert pinyin with numbers to real pinyin


import sys


VOWELS = "aeiouyü"

# Note that this will only catch lower case pinyin
pairs = {
	'a1' : 'ā',
	'a2' : 'á',
	'a3' : 'ǎ',
	'a4' : 'à',

	'e1' : 'ē',
	'e2' : 'é',
	'e3' : 'ě',
	'e4' : 'è',

	'i1' : 'ī',
	'i2' : 'í',
	'i3' : 'ǐ',
	'i4' : 'ì',

	'o1' : 'ō',
	'o2' : 'ó',
	'o3' : 'ǒ',
	'o4' : 'ò',

	'u1' : 'ū',
	'u2' : 'ú',
	'u3' : 'ǔ',
	'u4' : 'ù',

	'ü1' : 'ǖ',
	'ü2' : 'ǘ',
	'ü3' : 'ǚ',
	'ü4' : 'ǜ'
}


# Read file line by line and return its contents as a string
def readPinyin(file):
	str  = ""
	for line in file:
		str += line
	return str


# Write str to file
def writePinyin(file, str):
	file.write(str)


# Parse pinyin in 'vocab.txt' and output a new file 'parsed.txt'
def parse(input, output):

	file = open(input, 'r')
	pinyin = readPinyin(file)
	for p in pairs:
		pinyin = pinyin.replace(p, pairs[p])
	file.close()

	file = open(output, 'w')
	writePinyin(file, pinyin)
	file.close()


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('usage: python pinyin.py <input file> <output file>')
		exit(1)
	try:
		parse(sys.argv[1], sys.argv[2])
	except:
		print("Something failed. Exiting program.")
		exit(1)

