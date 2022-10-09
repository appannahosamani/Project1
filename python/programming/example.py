n=int(input("n= "))
if n>26:
    val=90
else:
    val=65+n-1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,n-i+1):
        print(val,end=" ")
        if (val>90):
            val=90
    val-=1
    print()
    if val<65:
        val=90
        