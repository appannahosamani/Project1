
class one:
    def __init__(self):
        self.x=10
        self.y=150

    def m1(self):
        print("iam m1")

class two:
    def __init__(self):
        self.a=100
    def m2(self):
        print("iam m2")

class three(one,two):
    def __init__(self):
        two.__init__(self)
        one.__init__(self)
        self.p=1000
    def m3(self):
        print("iam m3")

a1=three()
print(a1.__dict__)
a1.m1()
a1.m2()
a1.m3()