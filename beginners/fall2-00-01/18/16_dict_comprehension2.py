my_dict = {"a":1, "b":2 , "c":3}
my_dict2 = {"a": {"a1": 2}, "b": {"b1": 3} , "c": {"c1": 4}}

# if key == "a" and value != "b"
new_dict1 = {  key + "-asghar": value * 2 for key, value in my_dict.items() if key =="a" and value != "b" }

# no if else
# new_dict2 = {  key + "-asghar": value * 2 if key =="a" and value != "b" else key + "-asghar": value * 2  for key, value in my_dict.items()}
#                               items: {"a1": 2},  {"b1": 3}, {"c1": 4}
new_dict3 = {  key1: value1 for items in my_dict2.values() for key1, value1 in items.items()  }

print(new_dict1)
print(new_dict3)