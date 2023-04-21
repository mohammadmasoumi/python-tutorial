# 3
# 12
# 13
# 14

n = int(input()) # n: 4

my_list = []
idx = 0

while idx < n: 
    # idx: 0, n: 4, my_list: []
    # idx: 1, n: 4, my_list: [X, ]
    my_list.append(int(input()))
    # idx: 0, n: 4, my_list: [X, ]
    # idx: 1, n: 4, my_list: [X, X, ]
    idx += 1
    # idx: 1, n: 4, my_list: [X, ]
    # idx: 2, n: 4, my_list: [X, X, ]

print(my_list)