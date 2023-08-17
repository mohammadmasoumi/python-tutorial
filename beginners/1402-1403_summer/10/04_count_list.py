my_list = ["hello", "bye", "a", "a", 1, 1, 2, 2]
result = []

for item in my_list:
    has_seen, res_index = False, 0
    for idx, elem in enumerate(result):
        if elem[0] == item:
            has_seen, res_index = True, idx
            break
    
    if has_seen:
        result[res_index][1] += 1
    else:
        result.append([item, 1])

print(result)