# slicing
# ValueError: invalid literal for int() with base 10: 'Hello world'
# s = int("12")
s = "Hello world"

# [start_index:end_index(not included)]
# [1:3] => 1, 2
# [start_index:end_index:step]
# ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

print(s[1:3])
print(s[::])  # whole sting  خودش رشته را کامل چاپ میکند
print(s[::-1])
print(s[::-2])
print(s[5:-11:-1])

# AttributeError: 'str' object has no attribute 'reverse'
# print(s.reverse())

print("-----------------------------")
# cast str to list استرینگ را به لیست تبدیل کردیم
a = list(s)
print(f"list(s): {a}")
# a.reverse()
# print(f"list(s): {a}")

# ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# Hello
print("".join(a[:5]))
print(",".join(a[:5]))
print("-".join(a[:5]))
