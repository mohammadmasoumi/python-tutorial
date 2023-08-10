import time
import threading
import random
"""
FIFO

first in first out

push(1) -> append(1)
push(2) -> append(2)
push(3) -> append(3)

| 1  | 2  | 3  |   |   |   |   

pull -> pop(0) 
"""

# https://superfastpython.com/threadpool-producer-consumer/#:~:text=The%20producer%20tasks%20will%20put,the%20system%20using%20thread%20pools.

class Queue(list):

    def push(self, value):
        self.append(value)

    def pull(self):
        try:
            return self.pop(0)
        except IndexError:
            return None

queue = Queue()
# queue.push(1)
# queue.push(2)
# queue.push(3)

# queue: [1, 2, 3]
# print(queue.pull())
# queue: [2, 3]
# print(queue.pull())
# queue: [3]

counter = 0 

def producer():
    global counter

    while True:
        time.sleep(2)
        value = random.randint(1, 100)
        print(f"Producing: {value} ...")
        queue.push(value)

        counter += 1


def consumer():
    while True:
        time.sleep(1.9)
        print(f"Consuming: {queue.pull()} ...")


producer_thread = threading.Thread(target=producer, name='producer-thread')
consumer_thread = threading.Thread(target=consumer, name='consumer-thread')

producer_thread.start()
consumer_thread.start()


while True:
    time.sleep(1)
    if counter % 10 == 0:
        print(f"Bingo, you have produced {counter} messages!")

    if counter == 100:
        break

producer_thread.join()
consumer_thread.join()
