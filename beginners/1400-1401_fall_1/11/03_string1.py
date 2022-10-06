s = "Hello world"

sub_string = "Hello"
sub_string1 = "Asghar Agha"

# return True / False
print(f"boolean: {s.startswith(sub_string)}")

#
if s.startswith(sub_string):
    print(f'It starts with {sub_string}')
else:
    print(f"It does not start with {sub_string}")

#
if s.startswith(sub_string1):
    print(f'It starts with {sub_string1}')
else:
    print(f"It does not start with {sub_string1}")

print("------------------------------------------------")
# s = "Hello world"
# case sensitive - به کوچک و بزرگ بودن کاراکترها اهمیت میدهد
# sub_string2 = "world"
sub_string2 = "world"
sub_string3 = "Asghar Agha"

# s.endswith()
print(f"boolean: {s.endswith(sub_string2)}")

if s.endswith(sub_string2):
    print(f'It ends with {sub_string2}')
else:
    print(f"It does not end with {sub_string2}")

#
if s.endswith(sub_string3):
    print(f'It starts with {sub_string3}')
else:
    print(f"It does not start with {sub_string3}")


