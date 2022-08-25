# implementing stack data-structure
from collections import deque


class Stack:
    def __init__(self):
        self.box=deque()

    def push(self,value):
        self.box.append(value)

    def pop(self):
        self.box.pop()

    def top(self):
        return self.box[-1]

    def is_empty(self):
        return len(self.box)==0

    def size(self):
        return len(self.box)


if __name__ == '__main__':
    stack=Stack()
    stack.push(1)
    stack.push(5)
    stack.push(9)
    stack.push(67)

    print(stack.size())
    stack.pop()
    print(stack.box)
