# heLlo@worlD$hEllo#World^>1029
#       0        1
# [[character, count], [character, count], [character, count], ...]
# [
#   [h, 1],
#   [e, 1],
#   [l, 2],
# ...]

data = []

"""
1. character has been met 
    ++count

2. else
    add
    [character, 1]
"""
sentence = input()

for current_char in sentence:

    for item in data:
        # for char, count in data:
        # item: [current_char, count]
        # current_char: item[0]
        if item[0] == current_char:
            # if char == current_char:
            #     count += 1
            #     break
            item[1] += 1
            break
    else:
        data.append([current_char, 1])


def sort_function(item):
    # item: [character, count]
    return item[0]


# data.sort(key=sort_function)
print(data)
