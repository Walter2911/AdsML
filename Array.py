import random


class ArrayStack:
    def __init__(self):
        self.revdata = []
        self.data = []

    def __len__(self):
        return len(self.data)                   # 221910312015(K.L.S.Akash)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, ele):
        self.data.append(ele)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.data.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty")            # 221910312015(K.L.S.Akash)
        else:
            return self.data[0]

    def rev(self):
        while not self.is_empty():
            self.revdata.append(self.data.pop())


stack = ArrayStack()
print(f"Checking if the stack is empty or not: {stack.is_empty()}")
print(f"Trying to retrieve the first element: {stack.top()}")
print(f"Length of the stack: {stack.__len__()}")

for i in range(10):                                             # 221910312015(K.L.S.Akash)
    stack.push(random.randint(0, 100))

print(f"Stack after pushing elements: {stack.data}")
print(f"Retrieving the first element: {stack.top()}")
print(f"Checking if the stack is empty or not: {stack.is_empty()}")
print(f"Length of the stack: {stack.__len__()}")

for i in range(4, 9):
    x = stack.pop()
    print(f"Popped element: {x}")

print(f"Stack after popping elements: {stack.data}")
print(f"Length of the stack: {stack.__len__()}")
stack.rev()
print(f"Reversed Stack: {stack.revdata}")
