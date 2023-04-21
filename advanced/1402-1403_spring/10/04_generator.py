# generator is an iterator

# iterable -> iterator
# list -> iterator

# list X -> data generate
# memory efficiency

def generate_square(stop=10):
    for idx in range(1, stop+1):
        yield idx ** 2

gen = generate_square()
print(next(gen))
print(next(gen))

# next(gen)
for item in gen:
    print(item)
    break

print(next(gen))
print(next(gen))


# for item in generate_square():
#     print(item) 
