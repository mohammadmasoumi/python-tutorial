

def default_value_with_int(value=12):
    value += 1
    print(f"value: {value}, id(value): {id(value)}")


# NOT
# value: 13, id(value): 140727826683936
# value: 14, id(value): 140727826683936
# value: 15, id(value): 140727826683936
default_value_with_int()
default_value_with_int()
default_value_with_int()
