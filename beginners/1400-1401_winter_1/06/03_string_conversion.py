# srting conversion

print(12 > 13) # bool: False

"""
ab
bc
a ? b => b
"""
print("ab" > "bc")

"""
ac
ad
a ? a => =
c ? d => d > c
"""
print("ac" > "ad")

"""
a
ab
a ? a => =
  ? b => b
"""
print("a" > "ab") # False

"""
z
ab
z ? a => z > a
"""
print("z" > "abbbbbbbbbbbbbbbbbbbbbbbbbbbb") # True