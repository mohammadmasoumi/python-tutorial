
# [] => list
# {} => dict
my_dict = {"a":1, "b":2 , "c":3}
{"a": 1}

# more pythonic
new_dict = {  key + "-asghar": value * 2 for key, value in my_dict.items()  }
print(new_dict)

print("--------------------")
new_dict = {}
for key, value in my_dict.items():
    new_dict[key + "-asghar"] = value * 2 

print(new_dict)