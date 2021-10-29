char_a = "a"

# char -> ascii
print(ord(char_a))

# ascii code -> char
print(chr(97))

#
print(ord(chr(97)))

# TypeError: ord() expected string of length 1, but int found
# 57
print(ord("9"))
