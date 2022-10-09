#Password Validation
n=input("password= ")
U,L,S,N=False,False,False,False
for i in n:
    if ord('A')<=ord(i)<=ord('Z'):
        U=True
    elif ord('a')<=ord(i)<=ord('z'):
        L=True
     
    elif i in "0123456789":
        N=True
    else:
        S=True
    
if U==True and L==True and S==True and N==True:
    if len(n)>=6:
        print("valid")
    else:
        print("password atleast contains minimum 6 char")
else:
    print("invalid password")







