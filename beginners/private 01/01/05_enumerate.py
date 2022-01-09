my_list = [1, 2, 3, 4, 5]

for elem in enumerate(my_list):
    idx, item = elem
    print(f"elem: {elem}, idx: {idx}, item: {item}")

#  (0, 1) => tuple
#      idx item
# idx, item = elem | (0, 1)
# elem: (0, 1) => idx:0 , item: 1
# elem: (1, 2)
# elem: (2, 3)
# elem: (3, 4)
# elem: (4, 5)

for idx, item in enumerate(my_list):
    print(f"idx: {idx}, item: {item}")
