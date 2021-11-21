from konlpy.tag import Kkma
from random import choice
import hgtk

def gud():
    kkma = Kkma()
    p='혼자서 하루쯤 어디라도 가고 싶어지는 날이 있다. 반복된 일상에 지쳐갈 때, 혼자만의 시간이 필요할 때, 기분 전환을 하고 싶을 때 등 마음이 어지러울 때면 이를 전환하기 위한 여행이 간절해진다. 이런 때 떠나는 여행은 잠깐이어도 마음의 큰 위안이 되고 다시 돌아온 일상을 잘 살아내게 하는 힘이 된다. '
    o=kkma.nouns(p)
    a=choice(o)
    c = []
    d = ''
    for b in range(len(a)):
        c.append(hgtk.letter.decompose(a[b])[0])
    for b in range(len(c)):
        d = d + c[b]
    return a,d
