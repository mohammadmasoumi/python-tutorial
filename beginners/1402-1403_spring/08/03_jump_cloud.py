#       #  #     #  #     #
path = [1, 1, 0, 1, 1, 0, 1]

# jump count
jump = 1
pos = 0

while (pos + 1 != len(path) - 1) or (pos + 2 != len(path) - 1):
    if path[pos+2] == 1:
        jump += 1
        pos += 2
    else:
        jump += 1
        pos += 1

print(jump)