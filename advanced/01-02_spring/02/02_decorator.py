import time

time.perf_counter()

# def shout():
#     pass

# print(shout, type(shout))

# a = 12
# b = a

# # خروجی تابع shout را داخل متغییر yell میریزد
# yell = shout()
# # مقدار متغیر shout را داخل متغیر yell میریزد
# yell = shout

# decorator
def run_twice(func):
    def wrapper():
        print("before call ...")
        func()
        func()
        print("after call ...")

    return wrapper

@run_twice
def say_greeting():
    print("Hello How are you?")

# f = wrapper
# f = run_twice(say_greeting)
# f()

say_greeting()