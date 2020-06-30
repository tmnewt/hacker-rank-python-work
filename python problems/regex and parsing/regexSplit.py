# https://www.hackerrank.com/challenges/re-split/problem

import re

# split on non-digits
regex_pattern = r"\D"	

line = '100,000,000.000'
print("\n".join(re.split(regex_pattern, line)))

