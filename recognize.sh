
#!/bin/bash

set -e

python3  1_convert.py       words-recognize-num.txt    words-recognize-acc.txt
python3  2_collect.py       words-recognize-acc.txt    words-recognize-nice.txt
python3  3_practice.py      words-recognize-nice.txt
python3  4_build_table.py   words-recognize-nice.txt   words-recognize.html
