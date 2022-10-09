from operator import xor


a= int(input("a= "))
b=int(input("b= "))
#print("before swapping","a=",a,"b=",b)
print("before swapping:"f"a={a} b={b}")

'''temp=a
a=b
b=temp'''

'''a=a+b
b=a-b
a=a-b'''

'''a=a*b
b=a//b
a=a//b'''

a=a ^ b
b=a ^ b
a=a ^ b
print("after swapping:"f"a={a} b={b}")
