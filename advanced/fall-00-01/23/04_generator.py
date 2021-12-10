# yield
# memory efficient

"""
return



"""


def my_gen():
    """
    save state
    :return:
    """
    item = 0

    print("Hello1")
    item += 1
    yield item

    print("Hello2")
    item += 1
    yield item

    print("Hello3")
    item += 1
    yield item

    print("Hello4")
    item += 1
    yield item


# lazy function
gen = my_gen()  # create a generator
# do not execute the function

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # StopIteration
