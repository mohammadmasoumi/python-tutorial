a_tuple = (1, 2, 3)

for item in a_tuple:
    print(item)

for idx, item in enumerate(a_tuple):
    print(f"idx: {idx}, item: {item}")

for item in enumerate(a_tuple):
    # for idx, elem in enumerate(a_tuple):
    # idx, elem = item
    print(f"item: {item}, type: {type(item)}, idx: {item[0]}, elem: {item[1]}]")

for idx in range(len(a_tuple)):
    print(a_tuple[idx])
