"""
tuple

immutable
duplication is allowed (1, 2, 1, 3, 1)
different type of items (1, True, "hello", 0.0, [1, 2, 3], (1, 2, 3))

syntax: t = ("1", 1, 3)
"""

t1 = (1)  # redundant paranthesis
t2 = (1, 2)
t3 = (1, )

print(f"t1: {t1}, type(t1): {type(t1)}")
print(f"t2: {t2}, type(t2): {type(t2)}")
print(f"t3: {t3}, type(t3): {type(t3)}")

