from collections import defaultdict

company_name = input()

common_characters = defaultdict(int)

# advanced way with defaultdict
for char in company_name:
    common_characters[char] += 1

# beginner way
# common_characters = {}
# for char in company_name:
#     if common_characters.get(char):
#         common_characters[char] += 1
#     else:
#         common_characters[char] = 1

sorted_by_alphabet = {k: v for k, v in sorted(common_characters.items(), key=lambda x: x[0])}
sorted_by_value = {k: v for k, v in sorted(sorted_by_alphabet.items(), key=lambda x: -x[1])}

counter = 0
for key, value in sorted_by_value.items():
    counter += 1
    print(f"{key}: {value}")
    
    if counter == 3:
        break

