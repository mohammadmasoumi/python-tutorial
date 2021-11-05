def my_function(**kwargs):
    for k, v in kwargs.items():
        if k == "C":
            print(f"vc: {v}")
        print(k, v)


# def simple_func(a, b, c, d):
# همه ورودی ها اجباری است
# simple_func(a, b, c=1, d=2
# فقط دو متغیر اول اجباری است و بقیه اختیاری است
# default values must be immutable
def simple_func(a, b, c=1, d=(1, 2,)):
    print(f"a: {a}, b: {b}, c:{c}, d:{d}")


simple_func(10, 12)
simple_func(10, 12, 20, 30)
simple_func(b=10, a=12)
simple_func(b=10, a=12, c=20)  # no default value


# simple_func(a=10, 12)
# simple_func(10, a=12) ypeError: simple_func() got multiple values for argument 'a'
# simple_func(b=10, 12) Exception

def my_function1(a):
    # type(a) == str
    if isinstance(a, str):
        print("Is string")


my_function1(12)
my_function1("asghar")


# def my_function2(a, c, *b):
def my_function2(a, *b, c):
    print(f"a: {a}, b: {b}, c: {c}")


# TypeError: my_function2() missing 1 required keyword-only argument: 'c'
my_function2(12, 20, 20, 100, 10, c=10)


# my_function2(12, 20, 20, 100, c=10)
# my_function2(12, 20, 20, 100, 10)

# tuple
# list
# int
# a_list: list, a_tuple: tuple, a_dict: dic
#  return -> int
# do not force parameters have strict type
# func(param1: type) -> return type:
def my_function3(a_list: list, a_tuple: tuple, a_dict: dict) -> list:
    print(a_list)
    print(a_tuple)
    print(a_dict)

    return [10, 12]


my_function3([1, 2, 3], a_tuple=(1, 2), a_dict={"a": 1})
my_function3([1, 2, 3], a_tuple=(1, 2), a_dict={"a", 1})  # do not throw exception


def my_function4(a, b, c):
    # c += 3
    return a + 1, b + 2, c + 3, a + b + c


#
item = my_function4(10, 12, 14)  # no unpacking
a, b, c, d = my_function4(10, 12, 14)  # unpacking

print(item)
print(a, b, c, d)

# None python
# Null java, c, c#
# Undefined js
print(type(None))  # <class 'NoneType'>
