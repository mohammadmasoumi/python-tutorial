
# yield === return 
# keep the state
def generator():
    # 
    # 
    # first next
    counter = 1
    print("1 in yield")
    yield 1
    # 
    # 
    # second next
    counter += 10
    print("2 in yield")
    yield 2
    #
    #
    #
    counter += 10
    yield 3
    #
    #
    #
    print(f"Counter: {counter}")
    yield 4 


my_gen = generator()
print(next(my_gen)) # 1
print(next(my_gen)) # 2
print(next(my_gen))
print(next(my_gen))