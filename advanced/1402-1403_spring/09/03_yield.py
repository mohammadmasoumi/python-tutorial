# yield VS return 

def gen():
    # stateful 
    # preserve state
    a = 10

    print("Hello 1")
    yield a 

    a += 1
    print("Hello 2")
    yield a

    a += 1
    print("Hello 3")

    return a # StopIteration: 12


generator = gen()

print(next(generator))
print(next(generator))
# print(next(generator)) # StopIteration: 12

# Hello 1
# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\Python\advanced-python-winter1401\09\03_yield.py", line 26, in <module>
#     print(next(generator))
# StopIteration: 1

# def gen():
#     print("Hello 1")
#     return 1

#     print("Hello 2")
#     yield 2


# generator = gen()

# print(next(generator))

# for item in gen():
#     print(item)