# by using normal method to create list in sub lists[[]]
#[1,2,3,4,5,6,7,8,9,10,11,12,13] to when i give 2 the list will print like this
#[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13]]
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
n=int(input())
l2=[]
if n==0:
    print(l1)
    exit()
for i in range(0,len(l1),n):
    l3=[]
    for j in range(i,i+n):
        if j<len(l1):
            l3.append(l1[j])
    l2.append(l3)
print(l2)

# by using slicing method
# key=int(input())
# l2=[]
# for i in range(0,len(l1),key):
#     l2+=[l1[i:i+key]]
# print(l2)

