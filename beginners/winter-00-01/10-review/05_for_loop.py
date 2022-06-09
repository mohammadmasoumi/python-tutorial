
"""
range
enumerate
"""
names = ["ali", "mobina", "asghar", "akbar", "maryam"]

for name in names:
    print(name)

"""
range

# اگر یک پارامتر ورودی بدیم، صرفا پارامتر پایان رو قبول میکند.
range(end)
# اگر دو تا پارامتر ورودی بدیم، پارامتر شروع و پایان را قبول میکند.
range(start, end)
range(start, end, step)

my_range = range(10)

print(my_range)
# range object at X12309712379286

print(list(my_range))
# [0, 1, ..., 9]

for num in range(10):
    print(num)

# start, end
# -1, 0, ..., 9
range(-1, 10)
# -10, -8, ..., 8
range(-10, 10, 2)
"""

print(tuple(range(10)))
print(set(range(10)))
print(list(range(10)))

# range(5)
#            0        1         2        3         4
# names = ["ali", "mobina", "asghar", "akbar", "maryam"]
# "ali" = names[0], "mobina" = names[1], "asghar" = names[2]
# idx: 0, 1, 2, 3, 4
for idx in range(len(names)):
    name = names[idx]
    print(name)

print("------------------------------")
# item
# (0, 'ali') tuple
# (1, 'mobina') tuple
# (2, 'asghar') tuple
# (3, 'akbar') tuple
# (4, 'maryam') tuple
for item in enumerate(names):
    # idx, name = (0, 'ali') 
    # unpacking
    idx, name = item
    print(f"idx: {idx}, name: {name}")

print("------------------------------")
for idx, name in enumerate(names):
    print(f"idx: {idx}, name: {name}")

print("------------------------------")
# names = ["ali", "mobina", "asghar", "akbar", "maryam"]
# names[2: 4] = ["asghar", "akbar"]
for idx, name in enumerate(names[2: 4]):
    print(f"idx: {idx}, name: {name}")
