# list comprehension
# dict comprehension 

print(
    [item for item in [1, 2, 3] if item != 2]
    )
print(
    [item * 2 if item == 2 else item // 2 for item in [1, 2, 3]]
    )

my_list1 = [[1, 2 ,3], [4, 5, 6]]
my_list2 = [1, 2, 3, 4]

#  [      2 , 4 , 6, 8               ]
print(       [       items * 2 for items in my_list2     ]          )

#                           items: [1, 2 ,3]      item: 1 , 2 ,3
print(      [  item * 2 for items in my_list1 for item in items  ]   )
print(      [  item * 2 for items in my_list1 for item in items if item == 2 ]   )
print(      [  item * 2 if item == 2 else item / 2 for items in my_list1 for item in items]   )
print(      [  item * 2 if item == 2 else item // 2 for items in my_list1 for item in items]   )

# [0, 4, 1, 2, 2, 3]