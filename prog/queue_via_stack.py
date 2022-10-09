class stack:
    def __init__(self):
        self.elements=[]

    def len(self):
        return len(self.elements)
    
    def push(self,item):
        self.elements.append(item)
    
    def pop(self):
        if self.elements == []:
            print("no items for remove")
        return self.elements.pop(-1)

class Queue_stack(stack):
    def __init__(self):
        self.stack_one=stack()
        self.stack_two=stack()
    
    def enqueue(self,item):
        self.stack_one.push(item)
    
    def dequeue(self):
        while len(self.stack_one.elements):
            self.stack_two.push(self.stack_one.pop())
        res= self.stack_two.pop()
        while len(self.stack_two.elements):
            self.stack_one.push(self.stack_two.pop())
        return res

q=Queue_stack()
q.push("a")
q.push("b")
q.push("c")
q.push("d")
print(q.elements)
# qq=Queue_stack()
# qq.dequeue()