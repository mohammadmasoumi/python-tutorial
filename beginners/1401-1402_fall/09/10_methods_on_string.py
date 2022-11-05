# capitalize

# Converts the first character to upper case
print("hello world".capitalize())
print("1hello world".capitalize())

# title
# Converts the first character of each word to upper case
print("hello world".title())

word = "hello world"
print(word[:1] + "E" + word[2:])

# upper
# Converts a string into upper case
print("hello world".upper())

# lower
# Converts a string into lower case
print("HELLO2WORLD".lower())

# casefold [other language]
# Converts string into lower case
print("HELLO2WORLD".casefold())

# center()	
# Returns a centered string
print("hello".center(10))
#     h e l l o 
# - - - - - - - - - -
print("hello".center(11, "-"))
print("hello world".center(10, "*"))

# count()
# Returns the number of times a specified value occurs in a string
#      012345678910
print("hello world".count("e", 4 , 10))
print("hello world".count("e", 1 , 10))

# endswith()
# Returns true if the string ends with the specified value
print("hello world".endswith("d"))
print("hello world".endswith("world"))

# startswith()	
# Returns true if the string starts with the specified value
print("hello world".startswith("hello"))
print("hello world".startswith("h"))
print("hello world".startswith("world"))

# expandtabs()	
# Sets the tab size of the string
# 1 tab => 4 space
print("hello\tworld")
print("hello\tworld".expandtabs(20))

# \n
print("hello\nworld")


# find()	
# Searches the string for a specified value and returns the position of where it was found
print("hello world".find("hello"))
#                             value start end
print("hello world hello".find("hello", 1))

# print("hello world hello".find("asghar", 1))
print("----------------------------------------")
word = "hello hello hello"
start_index = 0 
for _ in range(len(word)):
    position = word.find("hello", start_index)

    if position == -1:
        break

    start_index = position + len("hello")

    print(position)


# Formats 
# specified values in a string

print("Hello {} How are you? {}".format("akbar", "asghar"))
print("Hello {name2} How are you? {name1}".format(name1="mina", name2="asghar"))
print("Hello {1} How are you? {0}".format("mina", "asghar"))

# index()	
# Searches the string for a specified value and returns the position of where it was found
# Raises ValueError when the substring is not found.
print("hello world hello world".index("w", 4, 10))
# ValueError: substring not found
# print("hello world hello world".index("asghar", 4, 10))

# isalnum()
# Returns True if all characters in the string are alphanumeric
print("hello world".isalnum())
print("hello2world".isalnum())
print("hello%world".isalnum())

# isalpha()
# Returns True if all characters in the string are in the alphabet
print("helloworld".isalpha())
print("hello world".isalpha())
print("hello2world".isalpha())
print("hello%world".isalpha())

# https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python
# isdigit() Returns True if all characters in the string are digits
# isdecimal() Returns True if all characters in the string are decimal
# isnumeric() Returns True if all characters in the string are numeric
"""
+-------------+-----------+-------------+----------------------------------+
| isdecimal() | isdigit() | isnumeric() |          Example                 |
+-------------+-----------+-------------+----------------------------------+
|    True     |    True   |    True     | "038", "੦੩੮", "０３８"           |
|  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"          |
|  False      |  False    |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"  |
|  False      |  False    |  False      | "abc", "38.0", "-38"             |
+-------------+-----------+-------------+----------------------------------+
"""

# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case

# join()	Joins the elements of an iterable to the end of the string
# all elements of list must string

print(" | ".join(["1", "2", "3"]))
print("-" * 37)
# |
# "           ", "           ", "           "
# "           |           |           "
# |           |           |           |
print("|" + "|".join(["".center(11), "".center(11), "".center(11)]) + "|")
print("-" * 37)
# TypeError: sequence item 0: expected str instance, int found
# print("|".join([1, 2, 3]))
# "1 | 2 | 3"
print("***".join(["1", "2", "3"]))
# "1***2***3"

# translate()  Returns a translated string
txt = "Hello Sam!"
# ValueError: the first two maketrans arguments must have equal length
# "HSe", "AP"
mytable = txt.maketrans("HS", "AP", "loam")
print(txt.translate(mytable))

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
print("hELLo World".swapcase())

# strip()	Returns a trimmed version of the string
print("   hELLo World   ".strip())
print("hELLo World".strip("h"))
print("**hELLo World**".strip("**"))

# rstrip()	Returns a right trim version of the string
print("   hELLo World   ".rstrip())

# lstrip()	Returns a left trim version of the string
print("   hELLo World   ".lstrip())


# 
print("   hELLo      World   ".split())

word = "   hELLo      World   "
new_word = ""

start_space = True
for index, char in enumerate(word):
    if not char.isspace():
        if not start:
            start = False
    else:
        if not start:
            start = True

    if start:
        new_word += char

print(new_word)

