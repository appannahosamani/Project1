l1=[10,20,30,40,50]
print(l1)
n=int(input("n= "))
c=0
for j in range(n%len(l1)):
    c+=1
    temp=l1[0]
    for i in range(len(l1)-1):
        l1[i]=l1[i+1]
    l1[len(l1)-1]=temp
print(l1)
print(c)