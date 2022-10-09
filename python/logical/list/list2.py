# l1=[7,9,2,4,3,6,7,9,8,4,10]
# even=0
# odd=0
# for i in range(len(l1)):#or -->for i in l1:
#     if l1[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"even={even} and odd={odd}")


#to check the given values how many times present in the list 
l1=[1,0,2,5,0,5,0,1,0,3,4,5,7,9]
n=int(input())
a=0

for i in l1:
    if i==n:
        a+=1
print(a)


