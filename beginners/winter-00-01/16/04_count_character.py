# n: "hello world"
n = input()

"""
[
    [character, count],
    [character, count],
    [character, count]
]
"""
my_list = []

# n: "hello world"
for character in n:
    # character: h, my_list: []
    # جون اولین بار است که میبینمش
    
    # my_list = [   ['h', 1], ['e', 1], ['l', 1]    ]
    for item in my_list:
        # item: ? ['h', 1]
        #   0   1
        # ['e', 1]: character
        if item[0] == character:
            item[1] += 1
            break
    else:
        my_list.append([character, 1])


print(my_list)
