# l1=[5,3,1,2,30,400,50,70,20,-10]
# c1=0
# c2=0
# for i in range(1,len(l1)):
#     c1+=1
#     key=l1[i]
#     j=i-1
#     while (l1[j]>key and j>=0):
#         c2+=1
#         l1[j+1]=l1[j]
#         j-=1
#         print(l1)
#     l1[j+1]=key
# print(l1)
# print(c1,c2)

# # n=8123621274
# # rem1=n/10
# # max=rem1
# # min=rem1

# # while n>0:
# #     rem=n%10
# #     if min>rem:
# #         min=rem
# #     if max<rem:
# #         max=rem
# #     n//=10
# # print(f"{max}=max and {min}=min")


s='the'
for i in s:
    print(i*2,end='')