#!usr/bin/python

import re
import sys

a = sys.argv[1]
patern = re.compile('(^\d{3}\\s-\d{3}-\d{4}$)|(\+1^\d{10}$)')

result = patern.match(a)
print result