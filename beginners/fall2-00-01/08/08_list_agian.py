# rename => refactor + rename
# def test():
#     print()

# list of string
fruits = ["apple", "orange", "orange" "watermelon", "apple", "cucumber"]

# 2d_array = []
two_d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(fruits[0])  # index - access
fruits.append("peach")
fruits.insert(1, "banana")

#              0        1         2            3         4
# fruits = ["apple", "banana", "orange", "watermelon", "peach"]
# fruit = "orange"
fruit = fruits.pop(2)  # index

# search from the left, remove the first occurrence of banana
fruits.remove("banana")  # item
# fruits.remove("banana")  # item

fruits.count("banana")  # count

print(fruits)

# if item does not exist, raise exception
# fruits.index("banana")
# print(fruits[2:].index("apple"))
#                         start end
# print(fruits.index("apple", 1, 2))
print(fruits.index("apple", 1, 3))

#                        0               1
# fruits[1: 3] => ['orangewatermelon', 'apple']
print(fruits[1: 3].index("apple"))
