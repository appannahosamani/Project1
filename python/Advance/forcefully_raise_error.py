
print('start')
l1=[1,2,3,4,5,6]
try:
    index=int(input( "index: "))
    
    if index>=len(l1) or index<=len(l1):
        raise IndexError
except IndexError as e:
    print("index is out of range")
    print(e)

else:
    print('hhhaghgsh')

finally:
    print('iam finally')
print("end")