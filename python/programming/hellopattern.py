n= int(input())
a=n//2+1
s='HELLO'

for i in range(n):
    for j in range(n):
        if i+j>=n-1 and j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(s[i],end=" ")
    for j in range(n):
        if i+j<=n-1 and i>=j:
            print("*",end=" ")
        # else:
        #     print(" ",end=" ")
    print()









# n=int(input("n= "))
# for i in range(n-1):
#     for j in range(n):
#         if i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

    
#     print()
# for i in range(n):
#         for j in range(n):
#             if i<=j:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
