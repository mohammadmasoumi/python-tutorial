#       #  #     #  #     #
path = [1, 1, 0, 1, 1, 0, 1]

# jump count
jump = 0
pos = 0

while pos != len(path)-1:
    if pos+2 <= len(path)-1 and path[pos+2] == 1:
        jump += 1
        pos += 2
    else:
        jump += 1
        pos += 1

print(jump)