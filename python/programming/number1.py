# program to count total odd and even number

n=int(input("n= "))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1

print(f"even={even} odd={odd}")