import time


class Timer:

    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.end = time.perf_counter()

        print(self.end - self.start)


with Timer():
    for item in range(1000):
        pass


