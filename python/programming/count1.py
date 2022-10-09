n=int(input("n= "))
even=0
odd=0
# while n>0:  
#     if n%10!=0:
#         if n%2==0:
#             even+=1
#         else:
#             odd+=1
#     n//=10
# print(even)
# print(odd)
while n>0:
    a=n%10
    if a==0:
        pass5
    elif a%2==0:
        even+=1
    else:
        odd+=1
    n//=10
print("even",even)
print("odd",odd)