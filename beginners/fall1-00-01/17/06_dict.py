"""
Changeable - mutable
key ordered - python 3.8 >
key Duplication is not allowed
value Duplication is allowed
"""

d = {
    "k": "v",
    "k1": "v",
    "k2": "v",
    "k2": "v1",
}

print(d.get("v"))
print(d.get("k2"))
