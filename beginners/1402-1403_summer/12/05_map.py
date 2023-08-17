# map

"""
function/method

OOP -> method
"""
"""
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
"""
# int as function
# cast
# int("12")

my_list = ["12", "13", "14"] 
result = map(int, my_list)

print(list(result))
# result = []
# for item in my_list:
#     result.append(int(item))


