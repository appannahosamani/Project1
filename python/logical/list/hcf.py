a=int(input())
b=int(input())
if a>0 and b>0:
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            print(i)
            break