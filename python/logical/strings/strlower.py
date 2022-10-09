s="SPIDERMAN"
s1=""

for i in s:
    if ord('A')<=ord(i)<=ord('Z'):
        c=ord(i)+32
        s1+=chr(c)
    else:
        s1+=i
print(s1)

#  for i in s:
#     if  ord('A')<=ord(i)<=ord("Z"):
#         c=ord(i)+32
#         s1+=chr(c)
#     else:
#         s1+=i
print(s1)