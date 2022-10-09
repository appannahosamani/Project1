#find the space index and count the all spaces in a string

s="spider man is a super hero"
s1=" "
count=0
space=1
for i in range(len(s)):
    if s[i]==s1: # or use directly if s[i]==" ":
        print("space",space,":",i)
        space+=1
        count +=1
print("Total no of spaces :",count)
