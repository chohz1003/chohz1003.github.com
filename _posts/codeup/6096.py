r=[]
for o in range(19):
    r.append(input().split())
b=int(input())
for c in range(b):
    a=input().split()
    a = [a[1], a[0]]
    for z in range(19):
        if r[z][int(a[0])-1]=='1':
            r[z][int(a[0])-1] = '0'
        else:
            r[z][int(a[0])-1] = '1'
    for z in range(19):
        if z==int(a[1])-1:
            for x in range(19):
                if r[z][x]=='1':
                    r[z][x] = '0'
                else:
                    r[z][x] = '1'
for g in range(19):
    for f in range(19):
        print(r[g][f],end=' ')
    print('')
