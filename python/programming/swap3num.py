a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

print("before swapping:",f"a={a} b={b} c={c}")
'''t=a
a=c
c=b
b=t

a=a*b*c
b=a//(b*c)
c=a//(b*c)
a=a//(b*c)'''

a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print("after swapping->",f"a={a} b={b} c={c}")


 