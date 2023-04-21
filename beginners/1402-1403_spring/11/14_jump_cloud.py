
"""
       O
path: [1,1,1,1,0,1,1,0,1]

"""
#                       8
# path = [1,1,1,1,0,1,1,0,1]
path = [1,1,1,1,0,1,1,0,1,1,1]
pos = 0
jump_cnt = 0

while pos < len(path) - 1:
    # pos: 0, len(path): 9
    # pos: 2, len(path): 9, jump_cnt: 1
    # pos: 3, len(path): 9, jump_cnt: 2
    # pos: 5, len(path): 9, jump_cnt: 3
    # pos: 6, len(path): 9, jump_cnt: 4
    # pos: 8, len(path): 9, jump_cnt: 3
    if (pos+2) <len(path) and path[pos+2] == 1:
        pos += 2
    else:
        pos += 1

    jump_cnt += 1

print(jump_cnt)