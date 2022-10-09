n= int(input("n= "))
for i in range(n):
    for j in range(n):
        
        '''if i in (0,n-1)or j in(0,n-1):'''
        '''if (i==0 or j==0) or (i==n-1 or j==n-1):'''
        '''if (i==0 or j==0) or (i==n-1 or j==n-1) or i==j or i+j==n-1:'''
        '''if i in (0,n-1) or j==n//2:I'''
        '''if j in (0,n-1) or i==j:N'''
        #if i in (0,0) or i in (n//2,0) or  j in (0,n-1):
        if j==0 or (i in (0,n-1)and j<=n//2+1) or (j==n-1 and i in (n//2-1,n//2+1,n//2)):
        
        
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()