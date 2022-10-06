dict1 = {"a": 1, "b":2}

# del dict1
del dict1["a"]
b_value = dict1.pop("b")

# KeyError
# dict1.pop(2)

# اگر مقدار پیش فرض براش تعریف نکنید خطا بر میگرداند
#                     key, default_value
two_value1 = dict1.pop(2, None)
two_value2 = dict1.pop(2, "Hello asghar")

print("two_value1: ", two_value1)
print("two_value2: ", two_value2)

# NameError: name 'dict1' is not defined. Did you mean: 'dict'?
print(dict1)
print(b_value)
dict1.update(c=10)
