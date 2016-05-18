#!/bin/bash

cd $(dirname $0)

set -e

python3  ../1_convert.py      ../vocabulary/words-write-num.txt   ../vocabulary/words-write-acc.txt
python3  ../2_collect.py      ../vocabulary/words-write-acc.txt   ../vocabulary/words-write-nice.txt
python3  ../3_practice.py     ../vocabulary/words-write-nice.txt
python3  ../4_build_table.py  ../vocabulary/words-write-nice.txt  ../vocabulary/words-write.html
