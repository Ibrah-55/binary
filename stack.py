class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            return self.stack.append(dataval)
        else:
            return False

    def peek(self):
        return self.stack.pop()

    def remove(self):
        if len(self.stack) <= 0:
            return 'NO element in the stack'
        else:
            return self.stack.pop()

    
astack = Stack()
astack.add('Mon')
astack.add('Tue')
astack.peek()
astack.add("wen")
astack.add('thu')
astack.add('fri')
# print(astack.peek().capitalize())

print(astack.remove().capitalize())
