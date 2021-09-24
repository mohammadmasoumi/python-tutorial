# output

# f-string - 3.6 >
a = 12
b = 13
c = 14
print(f"a: {a}")

# format
print("a: {}".format(a))
print("a: {}, b: {}".format(a, b))
print("a: {asghar}, b: {akbar}".format(asghar=a, akbar=b))
print("a: {asghar}, b: {akbar}".format(akbar=b, asghar=a))

print("\\")
print("\"hello\"")
print("hello")
print('"hello"')
print("'hello'")
# print(""hello"") syntax error
print("hello\t hello")
print("hello\n hello")
print("hello\a hello")
print("hello\53 hello")
