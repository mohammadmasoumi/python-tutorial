
my_list = [1,2,3,4]

my_iter = iter(my_list)
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break