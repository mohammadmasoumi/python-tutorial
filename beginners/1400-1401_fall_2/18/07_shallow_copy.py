# shallow copy

dict1 = {"a": 1, "b": [1, 2, 3]}
dict2 = dict1.copy()

print("[BEFORE] dict1: ", dict1)
print("[BEFORE] dict2: ", dict2)

dict1["c"] = 10
dict2["b"].append(4)

print("[AFTER] dict1: ", dict1)
print("[AFTER] dict2: ", dict2)





