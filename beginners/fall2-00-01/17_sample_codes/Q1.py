keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# beginner
my_dict = {}
for idx, item in enumerate(keys):
    my_dict[item] = values[idx] 

print(my_dict)

# advanced
print(list(zip(keys, values)))
print(dict(zip(keys, values)))