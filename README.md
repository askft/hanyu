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


## Installation / Usage

**Requirements:**
* [Python 3](https://www.python.org/downloads/)

**Mac OS X or GNU+Linux**

```
git clone https://github.com/AlexanderSkafte/hanyu.git
cd hanyu
./run.sh
```

**Windows**

(Instructions coming. Should be easy to run. Characters may mess things up
for you however.)


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

