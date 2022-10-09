from abc import ABC, abstractmethod
class myclass(ABC):
    def mymethod(self):
        print("iam mymethod")
    
    @abstractmethod
    def method(self):
        pass
class subclass(myclass):
    def method(self):
        print("iam subclass ")
s1=subclass()
s1.mymethod()
s1.method()