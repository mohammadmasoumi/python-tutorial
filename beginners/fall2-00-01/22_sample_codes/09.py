import string

def check_contains_all_eng_characters(string):
    common = {}

    for char in string:
        common[char] = 1

    return len(common.keys()) == 26


print(check_contains_all_eng_characters(string.ascii_lowercase))
print(check_contains_all_eng_characters("abcd"))