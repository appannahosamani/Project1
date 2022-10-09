s="string"
print(s)
def str_partition(n):
    a,b,c="","",""
    for i in range(len(s)):
        if s[i]==n:
            index=i
            break
        a=s[:index]
        b=n
        c=s[index+1:]
        return a,b,c
p=str_partition(input())
print(p)