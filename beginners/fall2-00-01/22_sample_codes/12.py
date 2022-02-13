from time import sleep


def say_hello():
    print("Hello")


def three_seconds_delay(func):
    sleep(3)
    func()


three_seconds_delay(say_hello)
