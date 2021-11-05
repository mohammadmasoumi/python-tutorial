a_list1 = [1, 2]
a_list2 = [1, 2]


# a_tuple = (1, 2, [1, 2])
a_tuple1 = (1, 2, a_list1)
a_tuple2 = (1, 2, a_list2)

print(f"a_tuple1: {id(a_tuple1)} | value: {a_tuple1}")
print(f"a_tuple2: {id(a_tuple2)} | value: {a_tuple2}")

a_list1.append(3)

print(f"value: {a_tuple1}")
print(f"value: {a_tuple2}")
