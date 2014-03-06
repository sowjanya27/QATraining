#!usr/bin/python

import re
import sys

a = sys.argv[1]
patern = re.compile((r'^\$?(\d*(\d\.?|\.\d{1,2}))$'))

result = patern.match(a)
print result

