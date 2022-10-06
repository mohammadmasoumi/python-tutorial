dict1 = {"a": 1, "b": 2}

key = 10
d = 20
# {"a": 1, "b": 2, "key":10}

# update
# .sort(key=method)
dict1.update(key=key)
dict1.update(c=key)
dict1.update(d=key)
# dict1.update(key=10)
# {"a": 1, "b": 2, "key":10}

dict1[key] = key
# dict1[10] = 10
# {"a": 1, "b": 2, 10:10}

my_key = "name"
my_value = "asghar"

dict1.update(my_key=my_value)
# {"my_key": "asghar"} correct
# {"name": "asghar"} wrong

dict1[my_key] = my_value
# {"name": "asghar"}

print(dict1)