#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Convert pinyin that uses numbers to denote tones (such as ni3 ha3o)
to pinyin that uses accents to denote tones (such as nǐ hǎo).
"""


import sys

from util import convert_to_acc


def main(input, output):

    with open(input, 'r', encoding='utf-8') as file:
        pinyin = ''.join([line for line in file])

    pinyin = convert_to_acc(pinyin)

    with open(output, 'w', encoding='utf-8') as file:
        file.write(pinyin)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python %s <input file> <output file>" % sys.argv[0])
        exit(1)
    main(sys.argv[1], sys.argv[2])
