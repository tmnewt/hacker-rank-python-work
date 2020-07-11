# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re
import email.utils

expr = re.compile(r'^([A-Za-z](?:[A-Za-z\.\-\_0-9]?)+@[A-Za-z]+\.[A-Za-z]{1,3})$')
n = int(input())
for _ in range(n):
    mail = email.utils.parseaddr(input())
    try:
        addr = re.match(expr, mail[1]).group(0)
        print(email.utils.formataddr(mail))
    except AttributeError:
        pass
