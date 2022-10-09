n=int(input('n= '))
a=n
sum=0
while n>0:
    rem= n%10
    fact=1
    for i in range( rem,0,-1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==a:
    print(f"{a} is a strong number")
else:
    print(f"{a} is  not a strong number")

    # using class

 