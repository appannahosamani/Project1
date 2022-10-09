
# def pop_s(l1,n=0):
#     if n in l1:
#         c=l1.pop(n)
#         print(c)
#     else:
#         print(l1.pop())
# pop_s([1,6,9,3,5,7],3)

# write a prog to remove element in a list then print

# l1=[10,20,30,40,50]
# n=int(input())
# l2=[]
# for i in range(len(l1)):
#     if n==i:
#         print(l1[n])

#         break
    
# else:
#     print("enter correct value")
    

l1=[10,20,30,40,50]
n= int(input())
l2=[]
for i in range(len(l1)):
    if i!=n:
        l2.append(l1[i])
    else:
        print(l1[i])
print(l2)


# by using slicing  and removing the purticular index positional value in  a list
# l1=[i for i in range(10,100,10)]
# print(l1)
# n=int(input())
# l1=l1[:n]+l1[n+1:]
# print(l1)