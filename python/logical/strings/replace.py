
s="spiderman"
print(s)

a=input()
b=input()
# for i in range(len(s)):
#     if s[i:i+len(a)]==a:
#         b=s[i+len(a):]
# print(b)
c=""
if a in s:
    
    c+=b
    
print(c)
print(c+s[len(a):])





# class string:
#     def __init__(self,s):
#         self.s=s

#     def str_replace(self,a,b):
#         self.a=a
#         self.b=b
#         return a,b


# s=string(input())
# s.str_replace(10,12)
