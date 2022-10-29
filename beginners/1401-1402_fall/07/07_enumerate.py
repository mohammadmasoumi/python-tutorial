
my_list = [1, 2, 3, 4]
print("-------------1-------------")
for item in my_list:
    print(item)

print("------------2--------------")
for item in range(len(my_list)):
    print(item)

print("------------3--------------")
for item in range(len(my_list)):
    print(item, my_list[item])

# enumerate

print("------------4--------------")
for item in enumerate(my_list):
    # (0, 1)
    # unpacking
    # index, elem = (0, 1)
    index, elem = item
    print(f"index: {index}, elem: {elem}, item: {item}")

for index, elem in enumerate(my_list):
    print(f"index: {index}, elem: {elem}")
    