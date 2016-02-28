# Hànyǔ

你好！

I'm learning Chinese. Feel free to join in.
Don't forget to make sure your browser supports Chinese characters.

Please do note that the content is under development and not complete in any
way, shape or form. I willl update this README file with more information
as time passes by.


## What is it?

By running the main script, you will be introduced to a program that will let
you practice your vocabulary by translating words.

## Practicing on you own words

You don't need to use the word list provided (which is for practicing Chinese).
You can make your own files with words in them. They have to abide by the
following format:

```
! Language 1, Language 2, Language 3


# Category 1

word1a - word1b - word1c
word2a - word2b - word2c
word3a - word3b - word3c

; use the semicolon character to make a comment


# Category 2

word4a - word4b - word4c
word5a - word5b - word5c
word6a - word6b - word6c
```

A line can have several definitions for a word, like the following line:

```
hello, hi - hola
```

Entering either "hello" or "hi" when translating "hola" will count as a correct
answer.

See the file `words-num.txt` or `words-acc.txt` for an example of such a file.

After creating the file, you can practice on the words like this:

```
python 2_collect.py  <word_file> <tmp_file>
python 3_practice.py <tmp_file>
```

where `<word_file>` is the file with words and their translations, and
`<tmp_file>` is just a file that's easy for `3_practicy.py` to parse. You can
safely remove `<tmp_file>` when you're done.

There is a script `example_run.sh` that does exactly the above. Run it and see.


## Installation / Usage

**Requirements:**
* [Python 3](https://www.python.org/downloads/)

The run script (`run.sh`) uses `python3`. You may need to change it to just
`python` (most likely if you are on Windows).

**Mac OS X or GNU+Linux**

```
git clone https://github.com/AlexanderSkafte/hanyu.git
cd hanyu
./run.sh
```

**Windows**

* Unless you've got a terminal with support for Unicode characters, you may run
into problems.
* The program has barely been tested on Windows, so I cannot guarantee that it
works well.

```
git clone https://github.com/AlexanderSkafte/hanyu.git
cd hanyu
run.sh
```


## Files

The descriptions below are incomplete; please refer to the files for more
information.

**`words-num.txt`** - Contains a list of words (English - Pinyin - 汉语).
The pinyin uses numbers instead of accents.

**`words-acc.txt`** - Contains a list of words (English - Pinyin - 汉语).
The pinyin uses accents instead of numbers. This file is generated.

**`words-nice.txt`** - Contains a list of words (English - Pinyin - 汉语).
The pinyin uses accents instead of numbers. This file only exists so that it
can be easily parsed by other files. This file is generated.

**`run.sh`** - small bash script that runs `1_convert.py`, `2_collect.py` and
`3_practice.py` with some arguments. This script runs the practice program.
This file generates two files:
 * `words-acc.txt` - Same as `words-num.txt` but with accents instead of numbers
   for the pinyin.
 * `words-nice.txt` - An easily parsed text file with all the words.

**`1_convert.py`** - Parses "tone numbered pinyin" (such as the one in
`words-num.txt`) to "real" pinyin with correct typographical accents.
This is so I can quickly add new words without looking for the correct letter.
Writes to a new file.

**`2_collect.py`** - Parses a file with words where every line is in on the
format `English - Pinyin - 汉语`. Empty lines and comment lines are ignored.
Will sort words into categories. Writes to a new file.

**`3_practice.py`** - Reads the words in `words-nice.txt` into a `Dictionary`
data structure defines in `dictionary.py`.

**`dictionary.py`** - A data structure that holds `Word` objects and can handle
categories.

**`word.py`** - A data structure that contains all translations of a word, and
which category the word belongs to. Internally, a word is stored for instance as
a list [['I', 'me'], ['wǒ'], ['我']].

**`util.py`** - Contains useful constants and functions that are used throughout
the rest of the programs.

