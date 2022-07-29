def all_even():
    n = 0
    while True:
        yield n
        n += 2


print(next(all_even()))
print(next(all_even()))
print(next(all_even()))
print(next(all_even()))
print(next(all_even()))
print(next(all_even()))
print(next(all_even()))
print("-------------------------------------")

my_gen = all_even()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))