a=input()
if a=='A':
    a=10
if a=='B':
    a=11
if a=='C':
    a=12
if a=='D':
    a=13
if a=='E':
    a=14
if a=='F':
    a=15
b=1
while b < 16:
    print('%X' % a, '*%X' % b, '=%X' % (a * b), sep='')
    b=b+1
