# l1=[]
# n=int(input("n= "))
# def app(l1,ele):
#     l1+=[ele]
#     return l1
# for i in range(n):
#     app(l1,int(input()))
# print(l1)

# func=lambda n:n*2 if n>10 else n*3
# print(f"1.) {func(12), func(2)}")
# 

# piramid two side
# s="abcdefghi"
# n= int(input())
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     for k in range(n):
#         if i>k:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
    
#     print()

# val=n*2-1
# for i in range(n):
    
#     for m in range(i):
#         print(" ",end=" ")
#     for o in range(val):
#         print("*",end=" ")
#     print()
#     val-=2

# n=int(input())
# a=int(input())
# b=int(input())
# for i in range(1,n+1):
#     print(a*i,b*i,end=" ")

# fibonacci
# n=int(input())
# a=0
# b=1
# for i in range(n):
    
#     print(a,end=" ")
#     a,b=b,a+b

# reversing the number
# n= int(input())
# s=0
# r=0
# while n>0:
#     s=n%10
#     r=r*10+s
    
#     print(s,end=" ")
#     n//=10
# print(r)

n=int(input())

for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
if n==0:
    print("not prime")
else:
    print("prime")