"""
Update
Changeable - Mutable
Mutable - Immutable

"""
fruits = ["orange", "banana", "apple", "cucumber", "peach"]

# append the item to the last of the list
fruits.append("watermelon")

# add "cherry" at index 9
#             index, item
fruits.insert(0, "cherry")

#                            2
#                        'lemon',
# ['cherry', 'orange',            'banana', 'apple', 'cucumber', 'peach', 'watermelon']
fruits.insert(2, "lemon")

#                                                                       'pineapple',
# ['cherry', 'orange', 'lemon', 'banana', 'apple', 'cucumber', 'peach',              'watermelon']
fruits.insert(-1, "pineapple")
fruits.append("apricot")

#                1             2
# ['cherry', 'orange',      'lemon', 'banana', 'apple', 'cucumber', 'peach', 'pineapple', 'watermelon', 'apricot', 'apricot']
fruits.insert(2, "apricot")
fruits.append("apricot")

print(fruits)
