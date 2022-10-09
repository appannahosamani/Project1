#achiving the bineary search in list
l1=[10,20,30,40,50,60,70,80]
n=int(input("n= "))
f=0
l=len(l1)-1
count=1
if n in l1:
    while f<=l:
        m=(f+l)//2
        if l1[m]<n:
            f=m+1
            count+=1
            
        elif l1[m]>n:
            l=m-1
            count+=1

            
        else:
            print(f"{n} is at the index {m}")
            print(f"number of iterations are {count}")
            break
else:
    print(f"{n} is not present in the list")
        
        

