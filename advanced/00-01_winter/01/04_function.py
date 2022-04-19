# pass by variable or pass by reference
# pass object reference by value
a_int = 12
a_list = [1, 2]

def pass_by_value(item):
    print(f"[pass_by_value]item: {item}, id(item): {id(item)}")
    item = 13
    print(f"[pass_by_value]item: {item}, id(item): {id(item)}")
    
def pass_by_reference(item):
    print(f"[pass_by_reference] item: {item}, id(item): {id(item)}")
    item.append(3)
    print(f"[pass_by_reference] item: {item}, id(item): {id(item)}")

print(f"[BEFORE] a_int: {a_int}, id(a_int): {id(a_int)}")
# print(f"[BEFORE] a_list: {a_list}, id(a_list): {id(a_list)}")

pass_by_value(a_int)
# pass_by_reference(a_list)

print(f"[AFTER] a_int: {a_int}, id(a_int): {id(a_int)}")
# print(f"[AFTER] a_list: {a_list}, id(a_list): {id(a_list)}")
