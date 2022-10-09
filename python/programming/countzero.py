n=int(input("n= "))
c=0
d=0
while n>0:  
    if n%10==0:
        c+=1
    n//=10
print(c)