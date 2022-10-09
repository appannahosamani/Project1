class age_lessor_error(Exception):
    def __init__(self,msg) :
        self.msg=msg
    def __str__(self) :
        return self.msg
class age_greater_error(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self) :
        return self.msg
try:
    age=int(input("age: "))
    if age<18:
        raise age_lessor_error("age is less than 18")
except age_lessor_error as e :
    print(e)
else:
    print("age is perfect")
finally:
    print('end')