# make obligation -> force using key value
# def my_function1(a, *b, d, e):
def my_function1(a, *, d, e):
    print(f"a: {a}, d: {d}, e: {e}")


my_function1(10, d=20, e=30)


# use as variable
# first class object
# def yell(text):
def shout(text):
    # text.upper()
    text = text.upper()
    return text
    # return text


# TypeError: shout() missing 1 required positional argument: 'text'
# yell = shout()
yell = shout
# <function shout at 0x0000024061DF8940>
print(yell)


# print(shout(input()))
# print(yell(input()))


# def func(*a, *b):
# def m_func(*a, *b):
#     print(a)


# def greeting(func, text, asghar="asghar", akbar="akbar"):
def greeting(func, text, *a):
    greet = func(text)
    print(greet)


def shout1(text):
    return text.upper()


def yell1(text):
    return text.lower()


# HOW ARE you?
s = "Hello"
# s = input()
greeting(shout1, s)
greeting(yell1, s)



