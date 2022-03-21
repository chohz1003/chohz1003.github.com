p=input()
o=p.split(' ')
d = 1
a=int(o[0])
b=int(o[1])
c=int(o[2])
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
