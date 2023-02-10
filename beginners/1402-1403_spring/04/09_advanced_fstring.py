# advanced fstring

# float
a = 112.1233423534539

print(f"{a: .4f}")
print(f"{a: .40f}")
print(f"{a:.3f}")
# ValueError: Invalid format specifier
# print(f"{a:    .30f}")
print(f"{a: 2.3f}")
print(f"{a: 0.3f}")
print(f"{a: 02.3f}")

# indentation
name = "ali"
age = 20

# - - - - - 
# - - a l i
# fill character from RIGHT
print(f"{name:>20}{age:>20}")
print(len("                 ali"))
print(len("                  20"))
print(f"{'aliasghartajikkhali':>10}{age:>10}")
print(len("        20"))

# fill character from LEFT
print(f"{name:<20}{age:<20}")
# ValueError: '=' alignment not allowed in string format specifier
# print(f"{name:=20}{age:=20}")
# print(f"{name:<=20}{age:<=20}")
print(f"{name:<20}|{age:<20}")
print(f"{name:-<20}|{age:<20}")
print(f"{name:-<20}|{age:+<20}")
print(f"{name:-<20}|{age:*>20}")
print(f"{name:-<20}|{age: >20}")
print(f"{name:&<20}|{age: >20}")


# int
print(f"{2:03}")
print(f"{12:03}")
print(f"{12:05}")

import time
for i in range(100):
    time.sleep(0.1)
    print(f"{i:003}")
    






