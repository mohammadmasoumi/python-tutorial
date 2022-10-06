d = {
    "k3": 300, 
    "k2": 20, 
    "k1": 1000, 
    "k4": 4, 
}

my_list1 = [("k1", 1), ("k2", 2), ("k3", 3)]
my_list2 = [["k1", 1], ["k2", 2], ["k3", 3]]
my_list3 = [{"k1", 1}, {"k2", 2}, {"k3", 3}]

print(dict(my_list1))
print(dict(my_list2))
print(dict(my_list3))

def sort_by_key(item):
    # item: ("k1", 1)
    key, value = item
    return key

def sort_by_value(item):
    key, value = item
    return value

def sort_by_key_value(item):
    key, value = item
    return abs(value  - 50)

# d.items() == [("k1", 1), ("k2", 2), ("k3", 3)]
# 
print(dict(sorted(d.items(), key=sort_by_key)))
print(dict(sorted(d.items(), key=sort_by_value)))
print(dict(sorted(d.items(), key=sort_by_key_value)))

print(sorted([-49, 2, 49, 0, 1, 51], key=lambda x: abs(x - 50), reverse=True))

ml = [-49, 2, 49, 0, 1, 51]
print(ml.sort(key=lambda x: abs(x - 50)))
print(ml)