# sequence - iterable
# index len

class Stack:
    
    def __init__(self):
        self.sequence = []
    
    def push(self, value):
        self.sequence.append(value)

    def pop(self):
        return self.sequence.pop()

    def __getitem__(self, idx):
        return self.sequence[idx]
    
    def __len__(self):
        return len(self.sequence)
    
    def __str__(self):
        return "[" + ", ".join([str(item) for item in self.sequence]) + "]"


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack[0])
print(stack)
print(type(stack))