#!/usr/bin/env python
# -*- coding: utf-8 -*-

PINK   = '\033[95m'
PURPLE = '\033[94m'
GREEN  = '\033[92m'
YELLOW = '\033[93m'
RED    = '\033[91m'
ENDC   = '\033[0m'

IDENTIFIER_COMMENT  = ';'
IDENTIFIER_CATEGORY = '#'
IDENTIFIER_LANGUAGE = '!'

DELIMITER_NUM       = '-'        # TODO Change this to something else (?)
DELIMITER_NICE      = ' | '        # Note the spaces


def iscomment(line):
    """Return true if line starts with IDENTIFIER_COMMENT."""
    return line.lstrip()[0] == IDENTIFIER_COMMENT


def iscategory(line):
    """Return true if line starts with IDENTIFIER_CATEGORY."""
    return line.lstrip()[0] == IDENTIFIER_CATEGORY


def islanguage(line):
    """Return true if line starts with IDENTIFIER_COMMENT."""
    return line.lstrip()[0] == IDENTIFIER_LANGUAGE


def split(s, delimiter):
    """Split a string "x delimiter y delimiter z"
    into a list ['x','y','z'].
    """
    return [w.strip() for w in s.split(delimiter)]


def convert_to_acc(pinyin):
    """Convert pinyin that uses numbers to denote tones (such as ni3 ha3o)
    to pinyin that uses accents to denote tones (such as nǐ hǎo).
    """
    for p in pairs:
        pinyin = pinyin.replace(p, pairs[p])
    return pinyin


def convert_to_num(pinyin):
    """Convert pinyin that uses accents to denote tones (such as nǐ hǎo)
    to pinyin that uses numbers to denote tones (such as ni3 ha3o).
    """
    for p in pairs:
        pinyin = pinyin.replace(pairs[p], p)
    return pinyin


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
