
#!/bin/bash

python convert.py vocab.txt pinyin.txt
python collect.py pinyin.txt

