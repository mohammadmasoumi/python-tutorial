# map
"""
built-in function
map obj = map(function, sequence)
"""
# print(float("1"))

list1 = ["1", "2", "3", "4", "5"]
print(list(map(float, list1)))

list2 = [10.1, 20.3, 30.5, 40.1, 50.9]

print(list(map(int, list2)))

"""
starts with character
case sensitive func Func
reserve keywords
between underscore, number
no other character than alphabetic
"""


def taha(item):
    # return int(item) // 10
    return int(item) // 10
    # return None


print(list2)
print(set(map(taha, list2)))

map_obj = map(taha, list2)
for item in map_obj:
    print(item)

# TypeError: 'map' object is not subscriptable
# print(map_obj[0])
