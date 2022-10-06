a = 10
b = 20
c = 30

print(f"{a} {a}          {a}")  # f-string - formatted string
print("{} {}          {}".format(a, a, a))
print("{} {}          {}".format(a, a, a, a))
# print("{} {}          {}".format(a, a)) # IndexError: Replacement index 2 out of range for positional args tuple
print("{} {}          {}".format(a, [a, a], a))
print("{a1} {a2}          {a3}".format(a2=c, a3=a, a1=b))

# escape character
print("-----------------------------")
print("'")
print('"')
print("\"")  # \ back slash
print('\'')  # \ back slash
# print(\)
print("\\")
print('\\')
print("-----------------------------")

print("Hello \nWorld")  # next line
print("\nHello \nWorld")  # next line

print("-----------------------------")
print("He\rllo World")  # carriage return - llo World
print("\rHello World")  # carriage return - Hello World
print("Hello World\r")  # carriage return - Hello World
print("Hello Wo\rrld")  # carriage return - rld
print("-----------------------------")

print("Hello\t W\torld")  # tab
print("-----------------------------")
print("\033Hello world")
print("\bHello\b w\borld")  # remove previous character
