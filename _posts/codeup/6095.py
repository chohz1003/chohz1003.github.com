a=int(input())
d=[]
for b in range(a):
    c=input().split()
    d.append(c)
p=''
for a in range(1,20):
    for b in range(1,20):
        for c in d:
            if c[0]==str(a) and c[1]==str(b):
                p='1'
                break
            else:
                p='0'
        print(p,end=' ')
    print('')
