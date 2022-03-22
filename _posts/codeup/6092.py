a=int(input())
c=input().split()
a=1
while a<24:
    d = 0
    for b in c:
        if int(b)==a:
            d=d+1
    print(str(d),end=' ')
    a = a + 1
