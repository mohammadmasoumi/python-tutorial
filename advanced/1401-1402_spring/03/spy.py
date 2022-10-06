METHODS = {}

"""
METHODS: {
    'func1': func1,
    'func2': func2,
}
"""


def register(func):

    def wrapper(*args, **kwargs):
        # args: tuple, kwargs: dict

        joint_args = " | ".join(map(str, args))
        joint_kwargs = " | ".join([ f"{k}-{v}" for k, v in kwargs.items()])

        with open("spy.txt", "a") as file:
            file.write(f"{func.__name__}: {joint_args}\n")
            file.write(f"{func.__name__}: {joint_kwargs}\n")
        
        # اسم تابع
        # func.__name__
        METHODS[func.__name__] = func

        # فراخوانی خود تابع اصلی با استفاده از ورودی‌هایی که بهش دادیم
        return func(*args, **kwargs)

    return wrapper


