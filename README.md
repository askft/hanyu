# Hànyǔ

你好！

I'm learning Chinese. Feel free to join in.
Don't forget to make sure your browser supports Chinese characters.

Please do note that the content is under development and not complete in any
way, shape or form. I willl update this README file with more information
as time passes by.

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

(Instructions coming. Should be easy to run.)


## Files

**`words-num.txt`** - contains a list of words (English - Pinyin - 汉语).
The pinyin uses numbers instead of accents.

**`run.sh`** - small bash script that runs `convert.py` and `collect.py` with
some arguments. Output files will be
 * `words-acc.txt` - same as `words-num.txt` but with accents instead of numbers
   for the pinyin.
 * `words-nice.txt` - an easily parsed text file with all the words.

**`convert.py`** - parses "tone numbered pinyin" (such as the one in
`words-num.txt`) to "real" pinyin with correct typographical accents.
This is so I can quickly add new words without looking for the correct letter.

**`collect.py`** - Parse a file with words where every line is in on the format
`English - Pinyin - 汉语`. Empty lines and lines starting with a `#` character
are ignored. Write to a new file.

