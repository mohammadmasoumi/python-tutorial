import time

gen = ("a")  # what ?
tuple = (1,)

print(gen)
print(type(gen))

print(tuple)
print(type(tuple))


def timer(func):
    def wrapper():
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()

        print(f"t2 - t1: {t2 - t1}")

    return wrapper


@timer
def exec_gen():
    my_gen = (item for item in range(10000000000))
    for item in my_gen:
        # print(item)
        pass


@timer
def exec_list():
    my_list = [item for item in range(10000000000)]

    for item in my_list:
        # print(item)
        pass


exec_gen()
exec_list()
