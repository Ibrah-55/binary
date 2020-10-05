class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, lval):
        if lval < self.data:
            if self.left is None:
                return str(lval) + ' Not Found!'
            return self.left.search(lval)
        elif lval > self.data:
            if self.right is None:
                return str(lval) + " Not Found!"
            return self.right.search(lval)
        else:
            print(str(self.data) + " Found")

    def Tree(self):
        if self.left:
            self.left.Tree()
        print(self.data)
        if self.right:
            self.right.Tree()


root = Node(12)
root.insert(3)
root.insert(6)
root.insert(25)
root.insert(78)

print(root.search(18))
print(root.search(6))
