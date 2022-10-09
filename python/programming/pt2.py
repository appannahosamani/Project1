n=int(input("n= "))
val=ord("E")
for i in range(n):
    for j in range(i+1):
        
        print(chr(val),end=" ")
        val+=1
        if val>ord("Z"):
            val=ord("E") 

    print()
       