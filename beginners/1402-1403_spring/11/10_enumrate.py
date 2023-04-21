# enumerate

"""
           0          1       2       3
HOTEL: ["asghar", "hassan", "amir", "ali"]

# immutable
print(HOTEL[0]) # "asghar"
HOTEL[0] = "taghi"
print(HOTEL[0]) # "taghi"

# mutable
           0          1       2       3         0         1         2       3
HOTEL: [["asghar", "hassan", "amir", "ali"], ["mina", "mobina", "maryam", "leila"]]

----------------------
HOTEL[1].append("fatemeh")
            0          1       2       3         0         1         2       3         4
HOTEL: [["asghar", "hassan", "amir", "ali"], ["mina", "mobina", "maryam", "leila", "fatemeh"]]

----------------------
HOTEL[1].insert(1, "zahra")
            0          1       2       3         0       1         2       3         4          5
HOTEL: [["asghar", "hassan", "amir", "ali"], ["mina", "zahra", "mobina", "maryam", "leila", "fatemeh"]]

----------------------
HOTEL[1][1] = "soghra"
            0          1       2       3         0       1         2       3         4          5
HOTEL: [["asghar", "hassan", "amir", "ali"], ["mina", "soghra", "mobina", "maryam", "leila", "fatemeh"]]
"""

my_list = [10, 20, 30, 40]
my_list.insert(4, 50) # append(50)
my_list.insert(10, 60) # append(50)

# [10, 20, 30, 40, 50]


# The old way
# idx = 0
# for item in my_list:
#     print(idx, item)
#     idx += 1

# update
# replacement

for item in enumerate(my_list):
    # (idx, value): (0, 10), (1, 20)
    # 1.
    idx = item[0]
    value = item[1]
    # 2.
    idx, value = item[0], item[1]
    # 3.
    idx, value = item
    
    print(idx, value, item)

print("--------------------------")
"""
unpacking

a, b = 12, 13
a, b = [12, 13]
"""

for item in enumerate(my_list):
    # (idx, value)
    idx, value = item
    print(idx, value, item)

print("--------------------------")

# idx, value = item
for idx, value in enumerate(my_list):
    print(idx, value)
