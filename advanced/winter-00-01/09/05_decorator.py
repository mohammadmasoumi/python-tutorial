# decorator

def run_twice(func):

    def wrapper():
        print("Calling ...") 
        func()
        func()
        func()
        print("closing ...") 

    return wrapper


# اگر بخواهیم قبل و بعد از فراخوانی یک تابع کاری را انجام دهیم ازش استفاده میکنیم
@run_twice
def greeting():
    print("greeting ...")


greeting()