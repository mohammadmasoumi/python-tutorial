my_list = [1, 2, 3, 4]

# 1
for item in my_list:
    print(f"item: {item}")
print("-------------------------------------")

# 2
for idx in range(len(my_list)):
    print(f"my_list[{idx}]: {my_list[idx]}")

print("-------------------------------------")
# 3
for idx, item in enumerate(my_list):
    print(f"my_list[{idx}]: {item}")

# 4
# while
"""
while condition:
    # code block
"""
print("---------------------------------")
idx = 0
# idx = 0
# len(my_list) = 4
# my_list = [1, 2, 3, 4]
my_list = [10, 20, 30, 40]

while idx < len(my_list):  # 4 < 4
    # my_list[3]: 40
    # Index out of range
    print(f"my_list[{idx}]: {my_list[idx]}")
    idx += 1  # idx = 4
    # end of block

# rest of code
