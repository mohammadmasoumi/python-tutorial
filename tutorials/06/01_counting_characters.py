# sorting and comparing strings are based on ascii code

# print(ord('a'))
# print(chr(67))

my_characters = [0] * 26
n = int(input())

for _ in range(n):
    char = input()
    my_characters[ord(char) - ord('a')] += 1

for idx, count in enumerate(my_characters):
    print(f"{chr(idx + ord('a'))}: {count}")