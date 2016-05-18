cd $(dirname $0)

python3 ../2_collect.py   ../vocabulary/example_words.txt ../vocabulary/example_tmp.txt
python3 ../3_practice.py  ../vocabulary/example_tmp.txt
