l1=[10,20,30,40,50,60,70,80]
f=0
l=len(l1)-1

n=int(input())#70
if n in l1:
    while f<=l:
        m=(f+l)//2
        if n > l1[m]:
            f=m+1
        elif n<l1[m]:
            l=m-1
        else:
            
            print(f"{n}  index is {m}")
            break
else:
    print("invalid number")
