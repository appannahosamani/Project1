# s1=" koolar sleep for eaighteen hours a day"
# l1=s1.split()
# l2=list(map(len,l1))
# # print(list(l2))
# print(l1)
# print(max(l2))
# res=None
# c=0
# for i in l1:
#     print(len(i))
#     if max(l2) ==len(i):
#         res=i
#         c+=1

#     if c==2:
#         break


l1=[1,2,3]
l2=[4,5,6]
l3= list(map(lambda n1,n2:n1+n2,l1,l2))
print(l3)