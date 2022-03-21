a=input()
b=a.split()
c=int(b[0])
d=int(b[1])
e=int(b[2])
f=int(b[3])-1
b=0
while b<f:
    c=(c*d)+e
    b=b+1
print(c)
