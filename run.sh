
#!/bin/bash

set -e

python3  1_convert.py       words-num.txt    words-acc.txt
python3  2_collect.py       words-acc.txt    words-nice.txt
python3  3_practice.py      words-nice.txt
python3  4_build_table.py   words-nice.txt   words.html

