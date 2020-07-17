# https://www.hackerrank.com/challenges/validating-uid/problem

import re

expr = re.compile(r'^(?:(\d)(?!.*\1)){3,}(?:([A-Z])(?!.*\2)){2,}(?:([a-z])(?!.*\3)){0,5}$')
for _ in range(int(input())):
    s = input()
    if len(s) != 10:
        print('Invalid')
    else:
        s = ''.join(sorted(s))
        if re.match(expr, s) == None:
            print('Invalid')
        else:
            print('Valid')
        

# some expressions which are not the answer but are useful

#   ^(?:([\dA-Za-z])(?!.*\1)){10}$
#   ^(?:([0-9A-Za-z])(?!.*\1)){10}$
#  both of these are useful for identifying strings of n lenght with
#  no reoccuring characters


test = '''74jK6yO6Ee
6LfK3X35w4
Wf7BH1y37y
h833NYf2w6
944A4NKtE2
AhBYw9r675
e74D412L2I
yDO9Ee83fJ
26e5Pe2CgN
W2IWtJ1F4O
96R5ZDJg72
7qE7yN3yG2
Ewq1I16L5G
44NDO46dN3
r57tH10OEj
J950g9O427
h7AFN4y5dt
y6847324DA
YD780V5355
SA1eqMY8Q5
5RrJ3MHr7f
5FVw2qr6C8
C1B6862S9Q
Wr3w4h1r5B
HBj29W1NNN
6Z893A119S
w8fK22T1qE
XAj3SJ900P
41726EHJIr
39CRJ283SJ
rMR5A445Xy
DwW8DO831h
2081wZ2H7C
JUKyD5LK2C
t9g61rr31e
7F245LTU5H
OQ44q3D7X8
LQ51B4964K
2W598V68M5
5RNW61f15X
5R9R61qOrR
d47YX9KDP8
2KR49Y3TZ7
F8IEqN5F4C
7BfC6dB84I
60X151J5YN
886Y1y8119
T62y5T73Ee
yWY6D0186w
WNYdTA75L1
1J2t1L98XU
S17hK7C1dW
66hwwg13O8
fR3Y7T1h29
9LD58Kfh9N
STCqX887EH
HEEy47ZYZ4
4PO62F6771
FHVG5g94Dt
AXP8L6CIj3
E2236T19FV
fG796qfqjA
1qB7XQ4VVB
XMB188I25T
77yS77UXtS
d72MJ4Rerf
OA778K96P2
2TB1YVIGNM
9JC86fM1L7
3w2F84OSw5
GOeGU49JDw
8428COZZ9C
WOPOX413H2
1h5dS6K3X8
Fq6FN44C6P
215JNy754j
7S6ArXe18K
8w95EHM45h
1qI970YtJ3
4Yd14rN1qL
X6543gO8QS
466w2w77M4
99YV0W3eK6
65LHZGLZ51
48D4yCP218
I114wM2DV8
hdC18gwNYN
4gh8XL4AtR
W5IGfSHj87
wU8g8C7XrN90
74jK6yO6Ee
6LfK3X35w4
Wf7BH1y37y
h833NYf2w6
944A4NKtE2
AhBYw9r675
e74D412L2I
yDO9Ee83fJ
26e5Pe2CgN
W2IWtJ1F4O
96R5ZDJg72
7qE7yN3yG2
Ewq1I16L5G
44NDO46dN3
r57tH10OEj
J950g9O427
h7AFN4y5dt
y6847324DA
YD780V5355
SA1eqMY8Q5
5RrJ3MHr7f
5FVw2qr6C8
C1B6862S9Q
Wr3w4h1r5B
HBj29W1NNN
6Z893A119S
w8fK22T1qE
XAj3SJ900P
41726EHJIr
39CRJ283SJ
rMR5A445Xy
DwW8DO831h
2081wZ2H7C
JUKyD5LK2C
t9g61rr31e
7F245LTU5H
OQ44q3D7X8
LQ51B4964K
2W598V68M5
5RNW61f15X
5R9R61qOrR
d47YX9KDP8
2KR49Y3TZ7
F8IEqN5F4C
7BfC6dB84I
60X151J5YN
886Y1y8119
T62y5T73Ee
yWY6D0186w
WNYdTA75L1
1J2t1L98XU
S17hK7C1dW
66hwwg13O8
fR3Y7T1h29
9LD58Kfh9N
STCqX887EH
HEEy47ZYZ4
4PO62F6771
FHVG5g94Dt
AXP8L6CIj3
E2236T19FV
fG796qfqjA
1qB7XQ4VVB
XMB188I25T
77yS77UXtS
d72MJ4Rerf
OA778K96P2
2TB1YVIGNM
9JC86fM1L7
3w2F84OSw5
GOeGU49JDw
8428COZZ9C
WOPOX413H2
1h5dS6K3X8
Fq6FN44C6P
215JNy754j
7S6ArXe18K
8w95EHM45h
1qI970YtJ3
4Yd14rN1qL
X6543gO8QS
466w2w77M4
99YV0W3eK6
65LHZGLZ51
48D4yCP218
I114wM2DV8
hdC18gwNYN
4gh8XL4AtR
W5IGfSHj87
'''

count = 1
for s in test.splitlines():
    if len(s) != 10:
        print(f'Line {count} Invalid')
    else:
        s = ''.join(sorted(s))
        if re.match(expr, s) == None:
            print(f'Line {count} Invalid')
        else:
            print(f'Line {count} Valid {s}')
    count +=1

#for s in test.splitlines():
#    print(''.join(sorted(s)))