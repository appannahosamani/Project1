l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
d={}
# d1={l1[i]:l2[i] for i in range(l1)}
# print(d1)
for i in range(len(l1)):
    d.update({l1[i]:l2[i]})
print(d)
