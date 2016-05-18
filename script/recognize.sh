#!/bin/bash

cd $(dirname $0)

set -e

python3  ../1_convert.py      ../vocabulary/words-recognize-num.txt   ../vocabulary/words-recognize-acc.txt
python3  ../2_collect.py      ../vocabulary/words-recognize-acc.txt   ../vocabulary/words-recognize-nice.txt
python3  ../3_practice.py     ../vocabulary/words-recognize-nice.txt
python3  ../4_build_table.py  ../vocabulary/words-recognize-nice.txt  ../vocabulary/words-recognize.html
