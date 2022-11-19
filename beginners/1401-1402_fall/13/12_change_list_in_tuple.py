tuple1 = ([1, 2], (10, 20))
print(tuple1[0], type(tuple1[0]))
tuple1[0].append(3)
print(tuple1[0], type(tuple1[0]))

for item in tuple1:
    if isinstance(item, list):
        item.append(100)

print(tuple1)

# -----------------------------------
tuple2 = ("a", "b")
tuple2 = list(tuple2)
tuple2[0] = "x"
tuple2 = tuple(tuple2)
print(tuple2)
