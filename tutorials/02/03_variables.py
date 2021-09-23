# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

anInt = 10
aString = "aString"

print(f"anInt: {anInt}")
print(f"aString: {aString}")

# dynamic type
x = 10
x = "x"
print(f"x: {x}")

# casting - builtin function
casted_str = str(3)
casted_int = int(3)
casted_float = float(3)

print(f"casted_str: {casted_str}")
print(f"casted_int: {casted_int}")
print(f"casted_float: {casted_float}")

# get the type
x1 = 10
x2 = 10.0
x3 = "string"

print(f"x1: {type(x1)}")
print(f"x2: {type(x2)}")
print(f"x3: {type(x3)}")

# double or single Quotes

single_quote_string = 'single_quote_string'
double_quote_string = "double_quote_string"

print(f"single_quote_string: {single_quote_string}")
print(f"double_quote_string: {double_quote_string}")
