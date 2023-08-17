"""
my_list = ["hello", "bye", "a", "a", 1, "world", 2]

[1]
#   0       1
["hello", "a"]
#   1
[1, 2]

[2]
[["hello", 1], ["a", 2], []]

[3]
#    items           count
["hello", "a", 1, | 1,2,1]

[4]
even index: items
odd index: count
    0     1   2   3
["hello", 1, "a", 2]

--
int, str, char ??
[1, 2, 3, 4, "hello", "a", "bye"]
--
data structure:
1.
[]
[]

2.
[[], []]

3.
[[[]],[[]], [[]]]

"""

my_list = ["hello", "bye", "a", "a", 1, 1, 2, 2]
result = []

"""
result: []
item: "hello"

1. first time
result.append(["hello", 1])

2. second time or ...
               0
result: [["hello", 1]]
                 0    1
result[0] => ["hello", 1]
result[0][1] += 1
result[0] => ["hello", 2]

first or second time -- ?? --
search on result

"""
result = []

"""
my_list = ["hello", "bye", "a", "a", 1, 2, 2]
result = [["hello", 1], ["bye", 1], ["a", 2]]

"""
for item in my_list:
    # Have you seen item or not?

    # item: "hello"
    has_seen = False
    res_index = 0 
    for idx, elem in enumerate(result):
        #           0    1
        #         item count
        # elem: ["hello", 1]
        if elem[0] == item:
            has_seen = True
            res_index = idx
            break
    
    if has_seen: # bool(has_seen)
        # ["hello", 1]
        result[res_index][1] += 1
    else:
        result.append([item, 1])

print(result)