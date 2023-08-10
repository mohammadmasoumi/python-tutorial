def sequence():
    for item in range(5):
        yield item + 1

def double(gen):
    for item in gen:
        yield item ** 2

def even(gen):
    for item in gen:
        if item % 2 == 0:
            yield item

gen = even(double(sequence()))
print(next(gen))
print(next(gen))