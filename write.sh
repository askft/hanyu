
#!/bin/bash

set -e

python3  1_convert.py       words-write-num.txt    words-write-acc.txt
python3  2_collect.py       words-write-acc.txt    words-write-nice.txt
python3  3_practice.py      words-write-nice.txt
python3  4_build_table.py   words-write-nice.txt   words-write.html
