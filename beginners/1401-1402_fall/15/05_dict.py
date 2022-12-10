# dict

# Changeable [Mutable]
# Ordered Keys

# int, str, float, bool, list, tuple, set, dict
# LinkedList, BST, Red&Black Trees,

# define dict
dict1 = {}

dict3 = {
    1: "Hello",
    True: "Bye"
}
dict4 = {
    True: "Hello",
    1: "Bye"
}
# 1. {True: "Hello"}
# 2. {True: "Bye"}
print(dict3) # {1: "Bye"}
print(dict4) # {True: "Bye"}

dict2 = {
    # key: value,
    "name": "Asghar",
    "city": "Varamin",
    "age": 20,
    "grade": 19.2,
    "is_male": True,
    "scores": [10, 11, 12],
    "sourses": {"math", "art", "..."},
    "abc": 20,
    "age": 21  # update the value of age key
}

# dict2 = {"name": "Asghar","city": "Varamin","age": 20,"grade": 19.2,"is_male": True,"scores": [10, 11, 12],"sourses": {"math", "art", "..."},}

# access
print(dict2["name"])
# KeyError: 'lastname'
# print(dict2["lastname"])

print(dict2.get("name"))
# print(dict2.get("lastname", None))
print(dict2.get("lastname"))
#                value,      default value
print(dict2.get("lastname", "ASGHARI"))

# update
# update or insert => upsert
# ordered keys
# dict2.get("lastname") = "ASGHARI" wrong
dict2["lastnamebefore"] = "AKBARI"
dict2["lastname"] = "AKBARI"
dict2["city"] = "Tehran"
dict2["lastnameafter"] = "AKBARI"

# pop
value = dict2.pop("city")
# KeyError: 'Tehran'
# value1 = dict2.pop("Tehran")
value1 = dict2.pop("Tehran", "DefaultValue")

print(dict2)
print(value)
print(value1)
