n=int(input())
# a=len(str(n))
b=n
d=n
sum=0
i=0
while n>0:
    n=n//10
    i+=1

    
while d>0:

    rem=d%10
    p=0
    
    p=rem**i
    sum=sum+p
    d=d//10
if sum==b:
    print(f"{b} is an armstrong number")
else:
    print(f"{b} is not an  armstrong number")

