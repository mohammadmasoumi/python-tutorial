# decorator

# closure
def multiplication(num):
    def multiply(n):
        return num * n

    return multiply


multiplication_3times = multiplication(3)  # num


# print(multiplication_3times(10))  # n
# print(multiplication_3times(20))  # n


# 1
def run_twice(func):
    def wrapper():
        # before
        print("before")

        func()
        func()

        # after
        print("after")

    return wrapper


# @ decorator
@run_twice
def greeting(a):
    print("Hello")


greeting()
