
my_list = [1, 2, 3, 4]


for item in my_list:
    # code block
    print(f"item: {item}")

print("-----------------------")
# accumulation
acc = 0

# my_list = [1, 2, 3, 4]
for elem in my_list:
    # elem: 1, acc: 0
    # elem: 2, acc: 1
    # elem: 3, acc: 3
    
    # print(f"item: {item}, acc: {acc}")
    print(f"elem: {elem}, acc: {acc}")

    # acc = acc + elem
    acc += elem
    # acc: 1, elem: 1
    # acc: 3, elem: 2

print(f"acc: {acc}")