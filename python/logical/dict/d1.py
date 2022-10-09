#create a user input dictionary

n=int(input())
d={}
# d['1']=10

for i in range(n):
    d.update({int(input()):int(input())})
print(d)