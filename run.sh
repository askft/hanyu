
#!/bin/bash

python convert.py words-num.txt words-acc.txt
python collect.py words-acc.txt words-nice.txt
python stuff.py words-nice.txt

