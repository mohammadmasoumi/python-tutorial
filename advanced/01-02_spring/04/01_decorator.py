import time 


def timer(func):
    # func: take_long_time_to_execute
    def wrapper():
        s1 = time.perf_counter()
        # s1: 110
        # باید func را اینجا فراخوانی کنیم
        # چون میخواهیم تایم قبل و بعد از اجرا را نگه داریم
        res = func()
        # بقیه کد اجرا نمیشود
        # return func()
        s2 = time.perf_counter()
        # s2: 200 
        # s2 - s1
        print(f"Duration: {s2 - s1}")

        return res

    return wrapper


@timer
def take_long_time_to_execute():
    for _ in range(100):
        for _ in range(100):
            print("Hello")

    return 10


a = take_long_time_to_execute()
# a = wrapper()
print(f"a: {a}")