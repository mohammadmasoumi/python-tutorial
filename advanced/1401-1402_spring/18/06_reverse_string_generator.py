my_string = "hello"

def revr(my_str):
    for idx in range(len(my_str)-1, -1, -1):
        yield my_str[idx]

my_gen = revr(my_str=my_string)

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

for item in my_gen:
    print(item)