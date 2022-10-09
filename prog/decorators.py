def smart_div(f):
    def inner(n,m):
        print("two")
        if n<m:
            n,m=m,n
        return f(n,m)
        
    print("one")
    return inner

# div= smart_div(div)
@smart_div
def div(a,b):
    print(a/b)
    print("three")
div(2,4)


