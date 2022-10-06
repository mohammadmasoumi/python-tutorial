# yield
# memory efficient

"""
return



"""


def my_gen(stop):
    """
    save state
    :return:
    """
    item = 0

    while item <= stop:
        item += 1
        print(f"Hello{item}")
        yield item


# جنریتور زیر مجموعه اینتروتور است
# lazy function
gen = my_gen(100)  # create a generator
# do not execute the function

for item in gen: # iterator
    print(item)
# print(next(gen)) # StopIteration
