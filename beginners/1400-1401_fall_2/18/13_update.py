dict1 = {"a": 1, "b":2}
dict2 = {"a": 3, "d":4}
dict3 = {"a": 1, "b":2, "a": 3, "d":4}
dict4 = {"a": 1, "b":2, "c": 1, "d":4}
dict5 = {
    "a": 1, 
    "b":2, 
    "c": 1, 
    "d":4
}
key = "name"
value = "asghar"
a = "name2"
b = "value2"
dict6 = {key: value, a: b}
dict7 = {key: value, "a": "b"}

# dict1.update(dict2)
# "a": 1, "b":2, "a": 3, "d":4 
# "b":2, "a": 3, "d":4 
# print(dict1)

#  "a": 3, "d":4 , "a": 1, "b":2
# "b":2, "a": 1, "d":4 
dict2.update(dict1)
print(dict2)
print(dict3)
print(dict6)
print(dict7)
