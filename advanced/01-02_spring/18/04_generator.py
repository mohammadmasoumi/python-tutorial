def my_gen():

    a = 1
    print(f"My a is 1: {a}")
    yield a

    a += 1 # a: 1
    print(f"My a is 2: {a}")
    yield a

    a += 1
    print(f"My a is 3 : {a}")
    yield a

    a += 1
    print(f"My a is 4: {a}")
    yield a

# lazy loading
my_generator = my_gen()

print(my_generator)
print("----------------------------")
print(next(my_generator))
print(next(my_generator))
print("----------------------------")
for item in my_generator:
    print(item)
print("----------------------------")
for item in my_generator:
    print(item)