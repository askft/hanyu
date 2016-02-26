
"""
Convert pinyin that uses numbers to denote tones (such as ni3 ha3o)
to pinyin that uses accents to denote tones (such as nǐ hǎo).
"""


import sys


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
	'ü4' : 'ǜ',

	'A1' : 'Ā',
	'A2' : 'Á',
	'A3' : 'Ǎ',
	'A4' : 'À',

	'E1' : 'Ē',
	'E2' : 'É',
	'E3' : 'Ě',
	'E4' : 'È',

	'I1' : 'Ī',
	'I2' : 'Í',
	'I3' : 'Ǐ',
	'I4' : 'Ì',

	'O1' : 'Ō',
	'O2' : 'Ó',
	'O3' : 'Ǒ',
	'O4' : 'Ò',

	'U1' : 'Ū',
	'U2' : 'Ú',
	'U3' : 'Ǔ',
	'U4' : 'Ù',

	'Ü1' : 'Ǖ',
	'Ü2' : 'Ǘ',
	'Ü3' : 'Ǚ',
	'Ü4' : 'Ǜ'
}


def main(input, output):

	with open(input, 'r') as file:
		pinyin = ''.join([line for line in file])

	for p in pairs:
		pinyin = pinyin.replace(p, pairs[p])

	with open(output, 'w') as file:
		file.write(pinyin)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: python %s <input file> <output file>" % sys.argv[0])
		exit(1)
	main(sys.argv[1], sys.argv[2])

