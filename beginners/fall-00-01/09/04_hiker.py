paths = input()

sea_level = 0
valleys_count = 0

# print(paths, type(paths))
for path in paths:
    # print(path)
    if path == 'D':
        sea_level -= 1
    else:
        sea_level += 1

    # print(f"sea_level: {sea_level}")

    if sea_level == 0 and path == 'U':
        valleys_count += 1

print(valleys_count)
