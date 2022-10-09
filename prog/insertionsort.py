l1=[2,1,25,2,3,4,5,8,2,1,21,2]
for i in range(1,len(l1)):
    key=l1[i]
    j=i-1

    while l1[j] > key and j>=0:
        l1[j+1]=l1[j]
        j-=1
    l1[j+1]=key
print(l1)