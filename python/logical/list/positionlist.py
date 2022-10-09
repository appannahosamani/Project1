l1=[10,20,20,40,50]
n=int(input())
count=0
for j in range(n%len(l1)):
    temp=l1[0]

    for i in range(len(l1)-1):
        l1[i]=l1[i+1]
        count+=1
    l1[len(l1)-1]=temp
print(l1)
print(count)