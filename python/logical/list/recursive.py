# def fun(n):
#     print(n,end=" ")
#     a=ord(n)
#     if a<ord("D"):
#         fun(chr(a+1))
#         print(n,end=" ")
# fun("A")

def fun(n):
    print(chr(n),end=" ")
    
    if n<68:
        fun(n+1)
        print(chr(n),end=" ")
fun(65)
