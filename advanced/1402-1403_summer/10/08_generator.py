def sequence():
    for item in range(5):
        yield item + 1

def double(gen):
    # gen: sequence()
    # item: next(gen)
    # item: 1
    # yield: 1
    for item in gen:
        yield item ** 2

# def cube(gen):
#     for item in gen:
#         yield item ** 3

def even(gen):
    # gen: double(sequence()
    # next: double(1)
    for item in gen:
        if item % 2 == 0:
            yield item

# even -> double -> sequence
gen = even(double(sequence()))
print(next(gen))
print(next(gen))