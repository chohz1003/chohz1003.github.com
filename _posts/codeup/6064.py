a=input()
b=a.split(' ')
if int(b[0])>int(b[1]):
    if int(b[1])>int(b[2]):
        print(b[2])
    else:
        print(b[1])
else:
    if int(b[0])>int(b[2]):
        print(b[2])
    else:
        print(b[0])
