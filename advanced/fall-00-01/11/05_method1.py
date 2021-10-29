def pass_by_value(param):  # pass by value for immutable

    if isinstance(param, int):
        param += 1

    elif isinstance(param, tuple):
        param = param + (2, 40, 20)
        param[2].append(10)

    print(id(param), param)


def pass_by_reference(param):  # pass by reference for mutable
    param.append(10)
    print(id(param), param)
    # return param


# --------------------------------
a_list = [1, 2, 3]

# a_list = pass_by_reference(a_list)
print(id(a_list), a_list)
pass_by_reference(a_list)
# pass_by_reference(&a_list)
print(id(a_list), a_list)

print(a_list)

print("----------------------------")
a_int = 3
print(id(a_int), a_int)
pass_by_value(a_int)
print(id(a_int), a_int)

print("----------------------------")

a_tuple = (1, 2, [1, 2, 3])
print(f"[BEFORE] id:{id(a_tuple)}, tuple:{a_tuple}")
pass_by_value(a_tuple)
print(f"[AFTER] id:{id(a_tuple)}, tuple:{a_tuple}")
