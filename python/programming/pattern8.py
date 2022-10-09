# n=int(input("n= "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#            print(val,end=" ")
#            val+=1
#            if val>9:
#                val=1
#         else:
#             print(" ",end=" ")
#     print()


# n= int(input("n="))
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("n= "))
# val=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#             val+=1
#             if val>ord('Z'):
#                 val=ord('A')
#         else:
#             print(" ",end=" ")
#     print()
n=int(input())
val=1
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(val,end=" ")
            val+=1
            if val>9:
                val=1
        else:
            print(" ",end=" ")
    print()