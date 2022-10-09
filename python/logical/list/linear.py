#to achive linear search using list
l1=[40,10,30,60,70,20,50,80]
n=int(input())
for i in range(len(l1)):
    if l1[i]==n:
        print(f"{i} is the index value of {n} ")
else:
    print(f"{n} is not present in the list")
    