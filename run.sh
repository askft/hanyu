
#!/bin/bash

python convert.py pinyin-num.txt pinyin-acc.txt
python collect.py pinyin-acc.txt pinyin-nice.txt

