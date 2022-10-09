n=int(input("n= "))
bin=0
i=0
while n!=0:
    rem=n%10
    bin=bin+rem*2**i
    n//=10
    i+=1
print(bin)