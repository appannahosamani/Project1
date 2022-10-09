n=int(input("n= "))
val=ord("Z")
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
            
        else:
            print(" ",end=" ")
    for j in range(n):
        if i+j<n-1:
            print(chr(val),end=" ")
            
            
        else:
            print(' ',end=' ')
    print()
    val-=1
    if val<ord("A"):
        val=ord("Z")
    