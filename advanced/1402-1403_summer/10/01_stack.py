"""
Stack

push pop

push(4)
push(5)
pop() # 5
push(6)

FILO - First In Last Out

|   |
|   |
| 6 |
| 4 |  
-----

my_stack = Stack()
my_stack.push(4)
my_statck.pop()

push
pop
print
"""

# class list:
#     def append(self, value):
#         pass

class Stack(list):
    def push(self, value):
        super().append(value)

    def pop(self):
        return super().pop()

stack = Stack()
stack.push(10)
stack.push(11)
stack.push(12)
print(stack.pop())
