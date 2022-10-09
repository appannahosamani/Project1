n=int(input("n= "))
if n>0:
    #if n%2==0:
    #if n/2==float(n//2):
    #if (n//2)*2==n:
    #if n & 1==0:
    #if (n&1)!=1:
    #if (n|1)==n:-->just reverse odd and even in print statements
    #if (n|1)==n+1:-->just reverse odd and even in print statements
    #if (n>>1)<<1==n:
    if (n>>1)<<1==n-1:#-->just reverse odd and even in print statements

        print(f"{n} is even")
    else:
        print(f"{n} is odd")