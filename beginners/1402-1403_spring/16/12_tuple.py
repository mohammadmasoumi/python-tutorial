# tuple

"""
# static list
Tuple: (immutable)
    (1, 2, 3, 4, 5)

#A1  #A2   #A3
[1]  [2]   [3]

X remove
X append
X insert

# dynamic list
List: (mutable)
    [1, 2, 3, 4, 5]

pointer
 #addreeValueOfIndex0
 0
[#22]

# 22
[1]

0 -> [1]
1
2
3
4
5
.
.
.
"""
a = 12
print(type(a))  # int

# redundant paranthesis
wrong_tuple = (1)
print(type(wrong_tuple))  # int

correct_tuple = (1,)
print(type(correct_tuple))  # type

# YOU CAN"T CAHNGE TUPLE (IMMUTABLE)
# correct_tuple.remove()
# correct_tuple.insert()
# correct_tuple.append()

# list WHY tuple ???
# - memory effiency

