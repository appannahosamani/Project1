#to check 2nd heighest marks
l1=[["appu",80],["rowdy",70],["krishh",70],["abc",80],["arya",90]]
a=0
m=0
for i in l1:
    if type(i)==list:
        for j in range(len(i)):
            if type(j)==list:
                for k in j:

                    if k==int:
                        m=k
                        if m>a:
                            a=m
                        else:
                            print(a)
                print(m)

                        


