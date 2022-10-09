# class jspider:
#     def rahul(self):
#         print("iam rahul")
    
# class qspider(jspider):
#     def rahul(self):
#         print("Iam doing training o c and c++")
# a1=qspider()
# a1.rahul()



# achice polymorphism wrt inheritace

class shape:
    def __init__(self):
        print("init method")
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    
    def area(self):
        return self.length * self.breadth

class circle(shape):
    def  __init__(self,pi,r):
        self.pi=pi
        self.rad=r
    def area(self):
        return self.pi *self.rad *self.rad
c1=circle(10,20)
print(c1.area())
r1=rectangle(3.142,5)
print(r1.area())


# def fun(**args):
#     print(args)

# fun(s="jhhjah",b="njzn", n3='kjskj')