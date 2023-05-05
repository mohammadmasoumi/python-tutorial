# meta programming
# type

string = "hello"

print(type(string), type(str))

for item in [int, str, float, list]:
    print(type(item))


print("------------------")
a = type(type)
print(type(a))
