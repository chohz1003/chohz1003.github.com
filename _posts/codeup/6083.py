a=input()
b=a.split(' ')
n=int(b[0])
m=int(b[1])
l=int(b[2])
a=0
for i in range(n) :
    for j in range(m) :
        for k in range(l):
            print(i, j, k)
            a=a+1
print(a)
