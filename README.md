# Hànyǔ

你好！

I'm learning Chinese. Feel free to join in.
Don't forget to make sure your browser supports Chinese characters.

Please do note that the content is under development and not complete in any
way, shape or form. I willl update this README file with more information
as time passes by.

## Usage

**Requirements:**
* [Python 3](https://www.python.org/downloads/)
* [PrettyTable](https://pypi.python.org/pypi/PrettyTable)

**Mac OS X or GNU+Linux**

```
git clone https://github.com/AlexanderSkafte/hanyu.git
cd hanyu
./run.sh
```


## Files

**`run.sh`** - small bash script that runs `convert.py` and `collect.py`.

**`vocab.txt`** - contains a list of words (English - Pinyin - 汉语).

**`convert.py`** - parses "tone numbered pinyin" to actual pinyin with correct
typographical accents. Will mess up indentation a little bit, but it shouldn't
be too big of an issue. This is so I can quickly add new words without searching
for the correct letter.

**`collect.py`** - Parse a file with words where every line is in on the format
`English - Pinyin - 汉语`. Empty lines and lines starting with a `#` character
are ignored.

