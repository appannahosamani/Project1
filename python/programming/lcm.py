a=int(input("a= "))
b=int(input("b= "))
for i in range(a,a*b+1):
    if i%a==0 and i%b==0:
        print(f" LCM of {a} and {b} is {i}")
        break