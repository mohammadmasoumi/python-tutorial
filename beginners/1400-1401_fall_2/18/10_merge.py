# **
# pack & unpack
# *[1, 2, 3] => 1, 2, 3

dict1 = {"a": 1, "b":2}
dict2 = {"c": 3, "d":4}

# **dict1
# "a": 1, "b":2
# **dict2
# "c": 3, "d":4
# **dict1, **dict2
# "a": 1, "b":2, "c": 3, "d":4
# {**dict1, **dict2}
# {"a": 1, "b":2, "c": 3, "d":4}
dict3 = {**dict1, **dict2}

print(dict1)
print(dict2)
print(dict3)