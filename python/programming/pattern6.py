# reverse piramid
# n=int(input("n="))
'''1st method
for i in range(n):
    for j in range(n):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    for j in range(n):
        if i+j<n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()'''


# val=n*2-1
# for i in range(n):
#     for k in range(i):
#         print(" ",end=" ")
#     for j in range(val):
#         print("*",end=" ")
#     print()
#     val-=2

n=int(input("n"))
val=n*2-1
val1=ord('A')
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(val):
        print(chr(val1),end=" ")
        val1+=1
        if val>ord('Z'):
            val=ord("A")
    print()
    val-=2
