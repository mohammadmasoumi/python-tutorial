# ASCII


# a -> 07
# A -> 65

# built-in ord
print(ord('a'))
print(ord('A'))

# boolean: True, False
print('a' < 'A')
print(97 < 65)

# ab
# aB
# - b > B
print('ab' < 'aB')

# ab
# b
# b>a
print('ab' < 'b')

# len      2    <    1
print(len('ab') < len('b'))

#
print('ab' < 'a')
print('aB' < 'a')
print('a' < 'aB')

# chr
print("--------------------------------")
print(ord("آ"))
print(ord("ژ"))
print(ord("ز"))
print(ord("گ"))

# TypeError: ord() expected a character, but string of length 2 found
# print(ord("ab"))

# TypeError: ord() takes exactly one argument (2 given)
# print(ord("a", "b"))
print(ord("a"), ord("b"))

print(chr(97))
print(chr(255))
print(chr(1000))
print(chr(2000))
print(chr(3000))
print(chr(30000))
print(chr(40000))
print(chr(1571))

#
print("----------------------------------")
# ord(chr(97))
# ord('a')
# 97
print(ord(chr(97)))
