#creating user input list
# n=int(input())
# l1=[]
# for i in range(n):
#     a=int(input())
#     l1.append(a)
# print(l1)


l1=[10,20,30,40,50]
temp=l1[0]
for i in range(len(l1)-1):
    l1[i]=l1[i+1]
l1[len(l1)-1]=temp
print(l1)    


# l3=[]
# l4=[]
# # a=l2.pop(0)
# # l2.append(a)
# # print(l2)
# for i in range(1,len(l2)):
    
#     l3.append(l2[i])
# for i in range(1):
#     l4.append(l2[i])
# print(l3)
# print(l3+l4)
