my_list = [20, 100, 200, 10]

for a in enumerate(my_list):
    # (0, 20)
    # v,a = (0, 20)
    # v = 0
    # a = 20
    v, c = a
    print(f"a: {a}")

for v, c in enumerate(my_list):
    print(f"v: {v}, c: {c}")
