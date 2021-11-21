from konlpy.tag import Kkma
from random import choice
import hgtk

def gud():
    kkma = Kkma()
    p=''
    a=choice(o)
    c = []
    d = ''
    for b in range(len(a)):
        c.append(hgtk.letter.decompose(a[b])[0])
    for b in range(len(c)):
        d = d + c[b]
    return a,d
