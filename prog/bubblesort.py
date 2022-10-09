l1=[2,4,1,3,5,6,1,2,3]
# l1=["abc","ahhgshg","ahh","as","a","akjahjgja","ahhj"]

for i in range(len(l1)-1):
    for j in range(len(l1)-1-i):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)

# l2=[2,4,1,3,5,6,1,2,3]
# l1=["abc","ahhgshg","ahh","as","a","akjahjgja","ahhj"]
# def sort(n):
#     for i in range(len(n)-1):
#         for j in range(len(n)-1):
#             if len(n[j]) > len(n[j+1]):
#                 n[j],n[j+1]=n[j+1],n[j]
#     print(n)

# sort(l1)
