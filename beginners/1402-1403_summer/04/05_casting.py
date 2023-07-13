# casting

# int -> str
# str -> int
# print

# builtin function
# int
# float
# str
# bool
# a = int(12) # 12

# int

# Falsy values:
# int: 0
# float: 0.0
# str: ""

# if 0: bool(0)
#     print("Hello")

print("-------------------- INT --------------------")

a1 = 12
a2 = 0
a3 = -1

print(f"int(a1): {int(a1)}")  # 12
print(f"int(a2): {int(a2)}")  # 0
print(f"int(a3): {int(a3)}")  # 01

print(f"str(a1): {str(a1)}")  # "12"
print(f"str(a2): {str(a2)}")  # "0"
print(f"str(a3): {str(a3)}")  # "-1"

print(f"float(a1): {float(a1)}")  # 12.0
print(f"float(a2): {float(a2)}")  # 0.0
print(f"float(a3): {float(a3)}")  # -1.0

# multiline cursor
# ctrl + shift + alt + ↑, ↓
print(f"bool(a1): {bool(a1)}")  # error, [True], False
print(f"bool(a2): {bool(a2)}")  # [False] Falsy value
print(f"bool(a3): {bool(a3)}")  # error, [True], False
# jump over a word: ctrl

print("-------------------- FLOAT --------------------")

b1 = 12.9
b2 = 0.0
b3 = -1.4

print(f"int(b1): {int(b1)}")  # 12 drop بخش اعشاری
print(f"int(b2): {int(b2)}")  # 0
print(f"int(b3): {int(b3)}")  # -1

print(f"str(b1): {str(b1)}")  # "12.9"
print(f"str(b2): {str(b2)}")  # "0.0"
print(f"str(b3): {str(b3)}")  # "-1.4"

print(f"float(b1): {float(b1)}")  # 12.9
print(f"float(b2): {float(b2)}")  # 0.0
print(f"float(b3): {float(b3)}")  # -1.4

print(f"bool(a1): {bool(a1)}")  # True
print(f"bool(a2): {bool(a2)}")  # False
print(f"bool(a3): {bool(a3)}")  # True

print("-------------------- STRING --------------------")

c1 = "ali"
c2 = ""
c3 = "12"
c4 = "12            "
c5 = "12            tom"  # "12            12", "12            12.2"
c6 = "tom"

# ValueError: invalid literal for int() with base 10: 'ali'
# convert to (1, 0), convert to ascii code, [exception], ali
# print(f"int(c1): {int(c1)}")
# ValueError: invalid literal for int() with base 10: ''
# print(f"int(c2): {int(c2)}") # "", [exception]
print(f"int(c3): {int(c3)}")  # [12], exception
# strip: remove additional spaces from beginning and end
print(f"int(c4): {int(c4)}")  # [12], exception,
# ValueError: invalid literal for int() with base 10: '12            a'
# print(f"int(c5): {int(c5)}")  # [exception]
# ValueError: invalid literal for int() with base 10: 'tom'
# print(f"int(c6): {int(c6)}")

print(f"str(c1): {str(c1)}")
print(f"str(c2): {str(c2)}")
print(f"str(c3): {str(c3)}")

# print(f"float(c1): {float(c1)}")  # the same as int, exception
# ValueError: could not convert string to float: ''
# print(f"float(c2): {float(c2)}")  # the same as int, exception
print(f"float(c3): {float(c3)}")  # the same as int, 12.0

# c1: "ali"
# c2: ""
# Expected output: True, False, Exception
print(f"bool(c1): {bool(c1)}")  # [True], False, Exception
print(f"bool(c2): {bool(c2)}")  # True, [False], Exception
print(f"{bool(' ')}")
# "\""
# print("''")
# print('""')
print(f"bool(c3): {bool(c3)}")  # True

print("-------------------- BOOL --------------------")

d1 = True  # 1
d2 = False  # 0

print(f"int(d1): {int(d1)}")  # [1], exception,
print(f"int(d2): {int(d2)}")  # 0

print(f"float(d1): {float(d1)}")  # 1.0
print(f"float(d2): {float(d2)}")  # 0.0

print(f"str(d1): {str(d1)}")  # exception, ["True"],
print(f"str(d2): {str(d2)}")  # False

print(f"bool(d1): {bool(d1)}")  # True
print(f"bool(d2): {bool(d2)}")  # False


# ctrl + x = CUT
# ctrl + c = COPY
# ctrl + v = PASTE
# ctrl + z = UNDO
# ctrl + shift + z = REDO
# ctrl + y = REDO
# ctrl + a = select all
# ctrl + s = SAVE
