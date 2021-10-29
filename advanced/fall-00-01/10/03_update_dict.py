d = {
    "a": 1,
    "a": 2
}

print(d["a"])

# update dict
tel_book = {
    "a": 12,
    "b": 13
}

tel_book["c"] = 14

# variable as key
name = "D"
tel_book[name] = 15  # "D": 15 - just once
tel_book["name"] = 15  # "name": 15
tel_book.update(name=15)  # "name": 15

# --------------------
tel_book["name"] = 15
tel_book.update(name1=16)  # add new key
tel_book.update(D=16)  # update key
tel_book.update(name=16, name1=17)  # update key
tel_book["a", "b"] = 1
# --------
a = 12, 20
a1 = (12, 20)
# a2 = (12)
print(type(a))
tel_book.update({"name": 20, "name1": 21})

print(tel_book)

# a = (10, 12, 20) tuple
# a, b = (10, 12, 20) unpacking - raise exception
a, *b, c = (10, 12, 20, 20)

# students = {
#     "name": ["ali", "hassan", "asghar"],
#     "mark": [[20, 20, 19], [20, 20, 19], [20, 20, 19]]
# }
#
# students = {
#     "ali": [20, 20, 19]
# }
