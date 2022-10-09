n=int(input("n="))
val=1
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(val,end=" ")
            val+=1
            if val>9:
                val=1
        else:
            print(" ",end=" ")

    print()