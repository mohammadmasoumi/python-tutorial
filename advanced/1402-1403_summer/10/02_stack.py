class Stack:
    """
    __dict__
    {
        "__init__": __init__,
        "__getitem__": __getitem__,
    }
    """
    def __init__(self):
        self.storage = []

    def __iter__(self):
        return iter(self.storage)

    def __getitem__(self, index):
        return self.storage[index]

    def __getitem__(self, index):
        return index + 1

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

stack = Stack()
stack.push(10)
stack.push(11)
stack.push(12)
print(stack.pop())

# next(stack) -> iterator
# ??
# print(next(stack))
print(stack[1]) # subscripable
print(Stack.__dict__)