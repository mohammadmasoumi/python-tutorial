# https://virgool.io/@amirvalizadeh/asterisks-in-python-yqme7tzc3lgi\

def run(n):
    def decorator(func):
        def wrapper():
            print("---------- Before ----------")
            
            for _ in range(n):
                func()
            
            print("---------- After ----------")

        return wrapper

    return decorator


# decorator
#@decorator
@run(10)
def greeting():
    print("Hello")


# @decorator
# def greeting():
#     print("Hello")


greeting()

