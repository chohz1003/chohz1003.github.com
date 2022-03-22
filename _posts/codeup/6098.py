r=[]
for o in range(10):
    r.append(input().split())
a=1
b=1
while r[a][b]!='2':
    if r[a+1][b]=='1' and r[a][b+1]=='1':
        break
    if r[a][b]=='0':
        r[a][b] = '9'
        if r[a][b+1]=='1':
            a=a+1
        else:
            b=b+1
r[a][b]='9'
for g in range(10):
    for f in range(10):
        print(r[g][f],end=' ')
    print('')
