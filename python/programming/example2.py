n=int(input("n= "))
val=ord('E')
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print(chr(val),end=" ")
            val+=1
            if val>ord('Z'):
                val=ord("A")
        else:
            print(" ",end=" ")
    print()