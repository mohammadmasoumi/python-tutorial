# my_list = [['a', 'b', 'c'], ['e', 'f', 'g']]
#
# if 'a' in my_list[0] and 'b' in my_list[0]:
#     # do sth
#     pass
#
# n = input()

# allowed_character = [['asgahr', 'asghare'], ['c']]
# for item in allowed_character:
#     if item not in n:
#         print("Wrong")
# ---------------------------------------------------------------
# print(ord('a'))
# print(chr(ord('a')))
# print(chr(97))

# n = int(input())
n = input()
repetition = [0] * 26

for character in n:
    # character = input()
    repetition[ord(character) - ord('a')] += 1

for idx, item in enumerate(repetition):
    if item:
        print(f"char: {chr(ord('a') + idx)}, count: {item}")
