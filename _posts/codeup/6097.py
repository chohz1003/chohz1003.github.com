a=input().split()
d=[]
for b in range(int(a[0])):
    p=''
    for c in range(int(a[1])):
        p=p+'0'+' '
    p=p[:-1]
    p=p.split()
    d.append(p)

b=int(input())
for c in range(b):
    p=input().split()
    if p[1]=='0':  #2 y 3 x
        l=-1
        for h in range(int(p[0])):
            l=l+1
            if d[int(p[2])-1][int(p[3])-1+l]=='0':
                d[int(p[2]) - 1][int(p[3]) - 1+l] ='1'
    else:
        l = -1
        for h in range(int(p[0])):
            l = l + 1
            if d[int(p[2]) - 1+ l][int(p[3]) - 1 ] == '0':
                d[int(p[2]) - 1+ l][int(p[3]) - 1 ] = '1'

for g in range(int(a[0])):
    for f in range(int(a[1])):
        print(d[g][f],end=' ')
    print('')
