# method_name = input()
method_name = "update"

set1 = {1, 2, 3}
set2 = {2, 4, 5}

print(dir(set1))

if method_name == "symmetric_difference_update":
    set1.symmetric_difference_update(set2)
elif method_name == "update":
    pass


# set1.
# def update(_set):
#     pass

# set1.symmetric_difference_update()
# set
# set1.update()
# set1.method_name()
# TypeError: asghar() takes 0 positional arguments but 1 was given
def asghar(s):
    # AttributeError: 'set' object has no attribute 'append'
    # s.append(1)
    pass


# AttributeError: 'set' object has no attribute 'asghar'
method = getattr(set1, "asghar", asghar)

# set1.update()
method(set2)

print(set1)

# def update(s):
#     s.update(s1)


attrs = [method for method in dir(set) if not method.startswith("__")]
for attr in attrs:
    try:
        m = getattr(set1, attr, asghar)
        print(f"{m}: {m(set2)}")
    except Exception as e:
        print(f"ERROR: {e}")

print(set1)
