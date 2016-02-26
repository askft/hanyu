
#!/bin/bash

set -e

python 1_convert.py words-num.txt  words-acc.txt
python 2_collect.py words-acc.txt  words-nice.txt
python 3_stuff.py   words-nice.txt

