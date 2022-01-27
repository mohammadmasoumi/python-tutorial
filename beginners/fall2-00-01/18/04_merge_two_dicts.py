dict1 = {"a": 1, "b":2}
dict2 = {"c": 3, "d":4}

# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'     
# {"a": 1, "b":2, "c": 3, "d":4}
# print(dict1 + dict2)

# dict' object has no attribute 'add'
# dict1.add(dict2)

# 
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("[BEFORE] dict1: ", dict1)
print("[BEFORE] dict2: ", dict2)
dict1.update(dict2)
dict1.update(e=10)
dict1.update({"e": 10})

print("[AFTER] dict1: ", dict1)
print("[AFTER] dict2: ", dict2)

# 
dict3 = dict1.copy()
dict3 = dict1

