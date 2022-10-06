# sort dict
d = {
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
    "k1": "v1",
}

d2 = {
    "k2": 101,
    "k3": 49,
    "k4": 51,
    "k1": 0,
}

# [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3'), ('k4', 'v4')]
# print(dict(
#         (
#             ("k1", "v1"), 
#             ("k2", "v2"),
#             ("k3", "v3"),
#         )
#     )
# )

# 
# my_list = [1, 50, 49, 10, 0] 

# def sort_function(value):
#     return -abs(value - 50)

# # my_list.sort(key=sort_function, reverse=True)
# my_list.sort(key=sort_function)
# print(my_list)

# d = {"k1": "v1","k2": "v2","k3": "v3","k4": "v4"}
# [("k1", "v1"), ("k2", "v2"), ("k3", "v3"), ("k4", "v4")]
def sort_function_based_on_key(item):
    # item: ('k1', 'v1') 
    key, value = item

    return key

def sort_function_based_on_value(item):
    # item: ('k1', 'v1') 
    key, value = item

    return value

def sort_function_based_on_value_distance_from_50(item):
    # item: ('k1', 'v1') 
    key, value = item

    return abs(value - 50)


# print(d.items())
# [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3'), ('k4', 'v4')]
# for item in [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3'), ('k4', 'v4')]:
#     sort_function(item)

print(dict(sorted(d.items(), key=sort_function_based_on_key)))
print(dict(sorted(d.items(), key=sort_function_based_on_value)))
print(dict(sorted(d2.items(), key=sort_function_based_on_value_distance_from_50)))