class Animals:
    def __init__(self):
        self.cat=[]
        self.dog=[]

    def enqueue(self,type,ani):
        if type=='cat':
            self.cat.append(ani)
        else:
            self.dog.append(ani)
    
    def dequeue_cat(self):
        if len(self.cat)==0:
            print("no cats")
        else:
            return self.cat.pop(0)
    
    def dequeue_dog(self):
        if len(self.dog)==0:
            print("no dogs present")
        else:
            self.dog.pop(0)
    
    def dequeue_animal(self,type):
        if type=='cat':
            if len(self.cat)>0:
                self.cat.pop(0)
            else:
                print('no cats present ')
        else:
            if len(self.dog)>0:
                self.dog.pop(0)
            else:
                print('no dogs are present')
anim=Animals()
# anim.dequeue_cat() 
# anim.dequeue_dog()    
anim.enqueue('dog','german')
print(anim.dog)
anim.enqueue('dog','german')
anim.enqueue('dog','lab')
anim.enqueue('dog','javari')
anim.enqueue('dog','jpan')

anim.enqueue('cat','india')
anim.enqueue('cat','himalayan')
anim.enqueue('cat','korea')
anim.enqueue('cat','german')

print(anim.cat,anim.dog)
print(anim.dequeue_cat())