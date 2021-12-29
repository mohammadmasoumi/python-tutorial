# input: Hellooooooooo
from typing import Counter


string = input()


# data_structure: [['H', 1], ['e', 1], ['l', 2], ...]
character_count_mapping = []

for char in string:


    # first: we should search for the character whether we've counted or not. if yes increase it's count
    for item in character_count_mapping:
        # item is like [characterm count]
        if char == item[0]:
            item[1] += 1
            break
    else:
        character_count_mapping.append([char, 1])


for char, count in character_count_mapping:
    print(f"{char}: {count}")