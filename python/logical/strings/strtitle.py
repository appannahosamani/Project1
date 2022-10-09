# input:-Spider man is a Superhero
# output:-Spider Man Is A Superhero

s="Spider man is a Superhero"
s1=' '
for i in range(len(s)):
    if i==0 or s[i-1]==" ":
        if ord('a')<=ord(s[i])<=ord('z'):
            c=ord(s[i])-32
            s1+=chr(c)
        else:
            s1+=s[i]
    else:
        s1+=s[i]
print(s1)
