d = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
}

"""
list comprehension
[item * 2  for item in []]
[item * 2  for item in [] if item % 2]
[item * 2 if item % 2 else item // 2 for item in []]

[1, 2, 3, 4, 5, 6]
[item for items in [[1, 2, 3], [4, 5, 6]] for item in items]
[item * 2 for items in [[1, 2, 3], [4, 5, 6]] for item in items if item % 2]
[item * 2 if item % 2 else item // 2 for items in [[1, 2, 3], [4, 5, 6]] for item in items]
"""

print({key + "Hello": value + "Hello" for key, value in d.items()})
print({key: value + "Hello" for key, value in d.items() if key == "k1"})
print({key + "Hello": value for key, value in d.items() if value == "v1"})
print({key : lambda x: x * 2 for key, value in d.items()})
print(d)

# f = lambda v: v * 2
# print(f, type(f))
# "k1"
# "k2"
# "k3"
# "k4"
# key: "k", v: "1"
for key, value in {key: (lambda : value * 2) for key, value in d.items()}:
    print(key, value)

for key, value in {key: (lambda : value * 2) for key, value in d.items()}.items():
    print(key, value())