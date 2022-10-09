a=int(input())
b=int(input())
try:
    c=a/b
except ZeroDivisionError as e:
    print(" values are not correct",e)
except ValueError as e:
    print('values are wrong')
else:
    print(c)
finally:
    print('Appu')
