# join

# lambda -> anoymouse function
def func1(x): return x * 2
def func2(x, y): return x + y

# func1 = lambda x: x * 2
# func2 = lambda x, y: x + y


print(func2(10, 12))
# print(func2(input(), input()))
# Application: map, filter

# filter -> filter
# map -> change all items of a list


# iterable
# all items of iterable must be string
scores = [1, 2, 3, 4, 5]

cast_to_str = str(scores)
#  0123456789 ...
# "[1, 2, 3, 4, 5]"
print(cast_to_str[4])
print(cast_to_str[0])

cast_to_list = []
for char in cast_to_str:
    cast_to_list.append(char)

print(cast_to_list)

print("-".join(str(scores)))
# scores = [1, 2, 3, 4, 5]
# str(scores)
# "[1, 2, 3, 4, 5]"
# ["[", "1", ",", " ", "2", ",", ...]
# ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']
# [-1-,- -2-,- -3-,- -4-,- -5-]

scores = [1,2,3,4,5]
print(str(scores)) # [1, 2, 3, 4, 5]
print("|".join(str(scores)))