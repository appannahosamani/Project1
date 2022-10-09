class myclass:
    x=10
    y=20
    def __init__(self):
        self.a=100
        self.b=200
    def mymethod(self):
        print("hi iam my method")
m1=myclass()
print(m1)
print("A value is-->", m1.a)
print("B value is->",m1.b)
print(myclass.x)
print(myclass.y)
m1.mymethod()