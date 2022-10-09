n=int(input(" n="))
for i in range(n):
    for j in range(n):
        # if(i+j<=n-1) and i>=j:  #1st method
        # 2nd method
        if (i+j>=n-1) and i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
#   3rd method  
# n= int(input("n="))
# for i in range(n//2+1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n//2+1,n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()    
