#          0 ---- len(my_list) -1
#  index   0  1  2  3
my_list = [1, 2, 3, 4]
#my_list = [10, 20, 30, 40]
#my_list.append(10)
#my_list.append(20)

#my_list.pop()
#my_list.pop()
#my_list.pop()
#my_list.pop()

# update - non-programatically
#my_list[0] = 2
#my_list[1] = 3
#my_list[2] = 4
#my_list[3] = 5  

# [1, 2, 3, 4]

# start, end(not included), step
#  range(start, stop[, step]
#                end
print(list(range(10))) # start=0, end=10, step=1 - range(0, 10)

#             start end
print(list(range(5, 10))) # step = 1

# [5, 7, 9]
print(list(range(5, 10, 2)))

# []
print(list(range(10, 5, 2)))

# [10, 8, 6]
print(list(range(10, 5, -2)))

# 0, 1, ...., len - 1 
# you can use idx or i or ...
# 0, 1, 2, 3
"""
i: 0
i: 1
i: 2
i: 3
"""
for i in range(len(my_list)):
    print(f"[BEFORE] my_list[{i}]: {my_list[i]}")
    # my_list[i] = my_list[i] + 1
    my_list[i] += 1
    print(f"[AFTER] my_list[{i}]: {my_list[i]}")
    print("----------------------------------")

# 0 1 2 3 - len:4
for item in my_list:
   # the value of room
   print(f"item: {item}")


