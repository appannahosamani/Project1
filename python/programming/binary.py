n=int(input("n= "))
bin=0
i=0
while n!=0:
    rem=n%2
    bin=bin+rem*10**i
    n//=2
    i+=1
print(bin)
