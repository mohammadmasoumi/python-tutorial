# cast


# int

# falsy value: 0

int_a = 12
int_b = str(int_a) # "12"
int_c = int(int_a) # 12
int_d = float(int_a) # 12.0
int_e = bool(int_a) # True
int_f  = bool(120) # True 
int_g = bool(0) # False
int_h = bool(-1) # True
int_l = bool(1000) # True
int_m = str(-1) # "-1"
# o = list(float_a) # TypeError: 'int' object is not iterable

print(f"int_a: {int_a}")
print(f"int_b: {int_b}")
print(f"int_c: {int_c}")
print(f"int_d: {int_d}")
print(f"int_e: {int_e}")
print(f"int_f: {int_f}")
print(f"int_g: {int_g}")
print(f"int_h: {int_h}")
print(f"int_l: {int_l}")
print(f"int_m: {int_m}")

# float

# falsy value: 0.0

float_a = 12.2
float_b = str(float_a) # "12.2"
float_c = int(float_a) # 12
float_d = int(12.8) # 12
float_e = bool(float_a) # True
float_f  = bool(0.0) # False 
float_g = bool(0.1) # True
float_h = bool(-1.1) # True
float_l = bool(1000.1) # True
float_m = str(-1.1) # "-1.1"
# o = list(float_a) # TypeError: 'float' object is not iterable

print(f"float_a: {float_a}")
print(f"float_b: {float_b}")
print(f"float_c: {float_c}")
print(f"float_d: {float_d}")
print(f"float_e: {float_e}")
print(f"float_f: {float_f}")
print(f"float_g: {float_g}")
print(f"float_h: {float_h}")
print(f"float_l: {float_l}")
print(f"float_m: {float_m}")

# str

str_a = "hello"
str_b = "12"
str_c = ""
str_d = "12        "
# str_e1 = int(str_a) # ascii_code, [exception]
str_e2 = int(str_b) # [12], exception
# str_e3 = int(str_c) # [exception]
str_e4 = int(str_d) # [12]
str_f1 = bool(str_a) # True
str_f2 = bool(str_b) # True
str_f3 = bool(str_c) # False
str_f4 = bool(str_d) # True
# ValueError: could not convert string to float: 'hello'
# str_g1 = float(str_a) # [exception] 
str_g2 = float(str_b) # 12.0
# str_g3 = float(str_c) # [exception]
str_g4 = float(str_d) # 12.0
str_h1 = str(str_a) # hello
str_h2 = str(str_b) # 12
str_h3 = str(str_c) # 
str_h4 = str(str_d) # 12    
str_l1 = list(str_a) # ["h", "e", "l", "l", "o"]
str_l2 = list(str_b) # ["1", "2"]
str_l3 = list(str_c) # []
str_l4 = list(str_d) # ["1", "2", " ", " "]

print(f"str_a: {str_a}")
print(f"str_b: {str_b}")
print(f"str_c: {str_c}")
print(f"str_d: {str_d}")
# print(f"str_e1: {str_e1}")
print(f"str_e2: {str_e2}")
# print(f"str_e3: {str_e3}")
print(f"str_e4: {str_e4}")
print(f"str_f1: {str_f1}")
print(f"str_f2: {str_f2}")
print(f"str_f3: {str_f3}")
print(f"str_f4: {str_f4}")
# print(f"str_g1: {str_g1}")
print(f"str_g2: {str_g2}")
# print(f"str_g3: {str_g3}")
print(f"str_g4: {str_g4}")
print(f"str_h1: {str_h1}")
print(f"str_h2: {str_h2}")
print(f"str_h3: {str_h3}")
print(f"str_h4: {str_h4}")
print(f"str_l1: {str_l1}")
print(f"str_l2: {str_l2}")
print(f"str_l3: {str_l3}")
print(f"str_l4: {str_l4}")
# ValueError: invalid literal for int() with base 10: '12abc'
# print(int("12abc"))
print(int("        12"))
# ValueError: invalid literal for int() with base 10: '        12    13          '
# print(int("        12    13          "))
print(bool(" "))

# ctrl + x = CUT
# ctrl + c = COPY
# ctrl + v = PASTE
# ctrl + z = UNDO
# ctrl + shift + z = REDO
# ctrl + y = REDO
# ctrl + a = select all
# ctrl + s = SAVE

