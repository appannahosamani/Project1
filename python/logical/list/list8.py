#l1=[1,2,[3,4,5],6,7,[8,9,10],11] to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  

l1=[1,2,[3,4,5],6,7,[8,9,10],11]
print(l1)
l2=[]
for i in l1:
    if type(i)==list:
        for j in i:
            l2.append(j)
    else:   
        l2.append(i)
print(l2)

