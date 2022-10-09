# the output will comes like this
# 1 : 6
# 2 : 14
# 3 : 22
# count 3


s="spider1 spider2 spider3"
c=0
s1="1,2,3,4,5,6,7,8,9,0"
d={}
for i in range(len(s)):
    if s[i] in s1:
        
        print(s[i],":",i)
        # d1=d.fromkeys(s[i],i)
        c+=1
        # print(d1)
print("count",c)

