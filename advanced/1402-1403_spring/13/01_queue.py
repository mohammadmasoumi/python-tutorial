
# FIFO
class Queue(list):

    def set(self, item):
        self.append(item)

    def get(self):
        try:
            return self.pop(0)
        except Exception:
            return None 
        

queue = Queue()
queue.set(1)
queue.set(2)

print(queue.get())
print(queue.get())
print("-------------------------")

# FILO
class Stack(list):

    def push(self, item):
        self.append(item)

    def pop(self):
        try:
            # self.pop()
            return super().pop()
        except Exception as e:
            print(e)
            return None 
        

stack = Stack()

stack.push(1)
stack.push(2)

print(stack.pop())
stack.push(3)
print(stack.pop())
