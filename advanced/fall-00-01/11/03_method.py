# method - function

# import requests
# requests.get("url")
# keyword
# def

# def func_name(params)
def print_hello():
    a = 20
    b = 30
    print("hello")
    return a + b


def add_three_numbers1(param1, param2, param3):
    return param1 + param2 + param3


def add_three_numbers2(param1, param2, param3):
    result = param1 + param2 + param3
    print(f"result: {result}")

    # return result
    # return None
    # return
    return 0


print_hello()
a = print_hello()
print(f"a: {a}")
print(f"{print_hello()}")

# add_three_numbers1() missing 3 required positional arguments: 'param1', 'param2', and 'param3'
# result1 = add_three_numbers1()
result1 = add_three_numbers1(10, 20, 19)
print(f"result1: {result1}")

# function call
# result2 = add_three_numbers2(10, 20, 19)
add_three_numbers2(10, 20, 19)
result2 = add_three_numbers2(10, 20, 19)
print(f"result2: {result2}")  # result2: None
