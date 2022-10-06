#        ["orange", "orange", "apple", "watermelon"]
#           1             2       4            3
fruits = ["orange", "orange", "watermelon", "apple"]


# ["a", "a", "b", "a"]
# ["apple", "apple", "b", "ax"]
# ["apple", "apple", "ax", "b"]

# orange
# orangei

# abc => ascci
# Abc => ascci

# orange <=> r
# orange <=> r
# watermelon <=> a
# apple <=> p
#  a            p      r       r
# watermelon, apple, orange, orange
def my_sort(item):
    # item: orange
    # item: orange
    # ...
    # return item[1]
    return item[-1]


# # سورت نزولی
fruits.sort(key=my_sort)
print(fruits)
# item ---> f ---> None
# def print_item(item):
#     # item: "orange"
#     # print(item)
#     # return None
#     #  "orange" + "hello" => orangehello
#     return item + "hello"
#
#
# # fruits = ["orange", "orange", "watermelon", "apple"]
# for fruit in fruits:
#     #                 "orange"
#     #  item    <=   "orangehello"
#     # item: "orangehello"
#     item = print_item(fruit)
#     print(item)
