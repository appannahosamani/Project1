n=int(input("n= "))

for i in range(n):
    for j in range(n):
        if j+i<=n-1 :
        #if j+i==n-1:
        #if j>=i:
        #if i+j==n-1 or i==j:
        #if i+j>=n-1:
        #if j<=i:
        #if i==j:

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
