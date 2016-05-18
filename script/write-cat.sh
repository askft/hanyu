#!/bin/bash

cd $(dirname $0)

set -e

python3  ../1_convert.py      ../vocabulary/words-write-cat-num.txt   ../vocabulary/words-write-cat-acc.txt
python3  ../2_collect.py      ../vocabulary/words-write-cat-acc.txt   ../vocabulary/words-write-cat-nice.txt
python3  ../3_practice.py     ../vocabulary/words-write-cat-nice.txt
python3  ../4_build_table.py  ../vocabulary/words-write-cat-nice.txt  ../vocabulary/words-write-cat.html
