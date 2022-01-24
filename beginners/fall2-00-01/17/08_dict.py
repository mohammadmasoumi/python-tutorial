# dict

# key <=> value
# 
from collections import defaultdict


personal_data = {
    "name": "ali",
    "age": 20,
    "avg": 10.2,
    "is_male": True,
    "courses": ["math", "PE", "art"],
    "nationality": "afghan",
}

# access to the element
print(personal_data)
# access to the value by key

#          value = obj[key]
print(personal_data["name"])
# KeyError: 'asghar'
# if key does not exist, raise exception
# print(personal_data["asghar"])

# -------------------------------
# if key does not exist: return default value. otherwise return value of specified key

#          value = obj.get(key)
print(personal_data.get("name", "Hello my name is asghar"))
#               obj.get(key, default_value)
#                               default_value: None
print(personal_data.get("asghar"))
#                             default_value: "Hello i am asghar" 
print(personal_data.get("asghar", "Hello i am asghar"))
print(personal_data.get("asghar", [1, 2, 3]))

key = "name"
default_value = "Hello i am asghar"
#                       "name", "Hello i am asghar" 
print(personal_data.get(key, default_value))
print(personal_data[key])
