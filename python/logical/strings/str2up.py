s="Spiderman"
s1=""
for i in s:
    if ord('a')<=ord(i)<=ord('z'):
        c=ord(i)-32
        s1+=chr(c)
    else:
        s1+=i
print(s1)
