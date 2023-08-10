def sequence():
    # memory
    # value
    # state
    # Keep function state instead of 1 to 100 numbers in Memory
    # Time Consumer
    # A little bit slow but memory efficient
    for idx in range(100):
        yield idx + 1  # Heavy calculation


my_sq = sequence()

print(next(my_sq))
print(next(my_sq))
print(next(my_sq))
print(next(my_sq))

for item in my_sq:
    print(f"item: {item}")
