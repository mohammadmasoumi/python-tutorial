# fstring
# formatted string

name = "Tom"

# Hello Tom, How are you? ...
print("Hello", name, ",How are you?")
print("Hello", name + ",How are you?")
print("Hello", name, ",", "How are you?")
print("Hello", name + ",", "How are you?")
print("Hello " + name + " How are you?")

# "123"
# "Tom,"
# "Tom" + "," => "Tom,"
# Hello, Tom
# "Hello " + name + " How are you?"

# "Hello, name How are you"
# {variable_name}
print(f"Hello {name}, How are you?")
