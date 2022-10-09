#bubble sort
l1=[5,3,1,2,30,400,50,70,20,10]
# l1.sort()
# print(l1)
l2=[]
c1=0
c2=0
c3=0
for j in range(len(l1)-1):
    c1+=1
    for i in range(len(l1)-1-j):
        c3+=1
        if l1[i]>l1[i+1]:#interchange (>) to (<) to get the descending order list
            l1[i],l1[i+1]=l1[i+1],l1[i]
            c2+=1
            
print(l1)
print(c1,c2,c3)