# inline input 

"""
1 2 3 4 5

"""
items = input() # items: "1 2 3 4 5"
print(items.split()) # default delimeter: " " 

"""
split

"1 2 3 4 5"
"1" "2 3 4 5" ["1"]
"2" "3 4 5" ["1", "2"]
"3" "4 5" ["1", "2", "3"]
...
["1", "2", "3", "4", "5"]
"""




# multiline input
"""
1
2
3
4
5
"""

# a = input()
# b = input()
# c = input()
# d = input()
# e = input()

# my_list = []

# for _ in range(5):
#     my_list.append(int(input()))


# print(a, b, c, d, e)
# print(my_list)