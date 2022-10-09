'''def num(*n):
    res=0
    for i in n:
        res=res+i
        return res
print(num(1,2,3,4,5))'''

def num(*n):
    a=0
    for i in n:
        a= a+i
       
    print("addition ->",a)
num(4,8,4)
#print(num(1,2,3))