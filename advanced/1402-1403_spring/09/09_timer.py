import time

class Timer:

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return lambda : self.end_time - self.start_time

    def __exit__(self, exc_type, exc_value, exc_tb):
        if not isinstance(exc_type, ValueError):
            self.end_time = time.perf_counter()


# timer: lambda : self.end_time - self.start_time
with Timer() as timer:
    for _ in range(10000):
        pass

print(timer())