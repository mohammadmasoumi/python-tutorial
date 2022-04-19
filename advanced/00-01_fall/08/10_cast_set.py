set1 = {1, 2, 3}
list_set1 = list(set1)
tuple_set1 = tuple(set1)
str_set1 = str(set1)

print(f"item: {list_set1}, type: {type(list_set1)}")
print(f"item: {tuple_set1}, type: {type(tuple_set1)}")
print(f"item: {str_set1}, type: {type(str_set1)}")

print(list_set1[1])
print(tuple_set1[1])
print(str_set1[0])

print("".join(str_set1[1: len(str_set1)-1].split(', ')))
