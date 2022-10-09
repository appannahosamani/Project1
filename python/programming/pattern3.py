# # # piramid
# # n=int(input("n= "))
# # for i in range(n):
# #     for j in range(n-1-i):
# #         print(' ',end=' ')
# #     for k in range(2*i+1):
# #         print("*", end=" ")

# #     print()


# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1 and i>=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
n=int(input())
val=ord('A')
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print(chr(val),end=" ")
        val+=1
        if val>ord('Z'):
            val=ord('A')
    print()
