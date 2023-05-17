#           0  1  2  3     4
my_tuple = (1, 2, 3, 4, [5, 6])

"""

1 2 3 4 *
        | 
        V
        [5, 6]


"""
# my_tuple[4]: list
my_tuple[4].append(7)

print(my_tuple)
