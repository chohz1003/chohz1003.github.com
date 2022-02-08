a=input('')
for b in range(1,int(a)+1):
    c=len(str(b))
    e=0
    for d in range(c):
        if str(b)[d]=='9' or str(b)[d]=='6' or str(b)[d]=='3':
            e=1
    if e==1:
        print('X',end = " ")
    else:
        print(b,end = " ")
