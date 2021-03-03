class Stack:
    def __init__(self):
        self.stack = []
        self.max_elem = None

    def __str__(self):
        ret = ""
        for x in self.stack:
            ret += str(x)
            ret += " "
        return ret

    __repr__ = __str__

    def getMax(self) -> int:
        return self.max_elem

    def push(self, elem: int):
        if self.max_elem is None:
            self.stack.append(elem)
            self.max_elem = elem
            return

        if elem > self.max_elem:
            tmp = elem * 2 - self.max_elem
            self.stack.append(tmp)
            self.max_elem = elem
        else:
            self.stack.append(elem)

    def pop(self) -> int:
        elem = self.stack.pop()

        if elem > self.max_elem:
            tmp = self.max_elem * 2 - elem
            elem = self.max_elem
            self.max_elem = tmp

        return elem


stack = Stack()
stack.push(-1)
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(-4)
stack.push(3)
stack.push(-2)


print(stack)
print(stack.getMax())
stack.pop()
print(stack.getMax())
stack.pop()
print(stack.getMax())
stack.pop()
print(stack.getMax())
stack.pop()
print(stack.getMax())
stack.pop()
print(stack.getMax())
