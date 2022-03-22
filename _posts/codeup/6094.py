a=int(input())
c=input()
c=c.split()
a=10000000000000000000000000000000000000000000
for b in c:
    if int(b)<a:
        a=int(b)
print(a)
