l=[10,[20,30],60,80,[40,50]]
l1=[]
for i in l:
    if type(i)==list:
        for j in i:
            l1.append(j)
    else:
        l1.append(i)
print(l1)