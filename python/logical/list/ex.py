#checking the how many even and odd numbers are present in the given numbe 
n=int(input())
even=0
odd=0
while n>0:
    a=n%10
    if a==0:
        pass
    elif a%2==0:
        even+=1
    else:
        odd+=1
    n//=10
print(f" number of odd:{odd}")
print(f" number of even:{even}")