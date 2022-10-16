# methods on string

string = "hello world"

# Converts the first character to upper case
# "Hello world" , "hello world"

# "hello world" => "Hello world"
print(string.capitalize(), string)

# "hello world" => "Hello World"
print(string.title(), string)

# Converts string into lower case
print("HELLO WORLD".casefold())
print("HELLO WORLD".lower())

# ---------------------------------
# For example, the German lowercase letter 'ß' is equivalent to 'ss'. Since it is already lowercase, 
# the lower() method would not convert it; whereas the casefold() converts it to 'ss'.
mystr = 'außen'
print(mystr.casefold())

mystr = 'außen'
print(mystr.lower())
# aussen
# außen
# ---------------------------------

# center()	Returns a centered string
# - - - - - B - - - - -
print("B".center(11))
print("B".center(11, "*"))
print("ALI".center(11,"-"))
print("AB".center(11))

# count()	Returns the number of times a specified value occurs in a string
print("hello world".count("l")) 

# endswith()	Returns true if the string ends with the specified value
print("hello world".endswith("d")) 
print("hello world".endswith("rld")) 
print("hello world".endswith("o")) 
print("hello world".startswith("o")) 


# expandtabs()	Sets the tab size of the string
print("\thello\tworld\t".expandtabs(20)) 

# Searches the string for a specified value and returns the position of where it was found
print("hello world".find("l")) # return index of the character or sub-string
#                  substring, start, end 
print("hello world".find("l", 4))
print("hello world".find("world")) # 6

# f-string f"{}"
# format()	Formats specified values in a string
name1 = "mohammad"
name2 = "ali"
name3 = "asghar"
print("hello {b}, hello {c}, hello {a}".format(a=name1, b=name2, c=name3))
print("hello {2}, hello {0}, hello {1}".format(name1, name2, name3))

# index()	Searches the string for a specified value and returns the position of where it was found
#                        substring, start, end
print("hello world".index("ello"))

# isalnum()	Returns True if all characters in the string are alphanumeric
print("hello!world".isalnum())
print("hello2world".isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
print("helloworld".isalpha())
print("hello2world".isalpha())

# isascii()	Returns True if all characters in the string are ascii characters

# https://www.w3schools.com/python/ref_string_isdecimal.asp
# isdecimal()	Returns True if all characters in the string are decimals
# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method is used on unicode objects.
print("003984792364".isdecimal())
print("²03984792364".isdecimal())

# https://www.w3schools.com/python/ref_string_isdigit.asp
# isdigit()	Returns True if all characters in the string are digits
# The isdigit() method returns True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.
print("²03984792364".isdigit())
print("-1".isdigit())

# https://www.w3schools.com/python/ref_string_isnumeric.asp
# isnumeric()	Returns True if all characters in the string are numeric
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
print("¾".isnumeric())

# isidentifier()	Returns True if the string is an identifier
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
# A valid identifier cannot start with a number, or contain any spaces.
print("last_name".isidentifier())
print("1last_name".isidentifier())

# islower()	Returns True if all characters in the string are lower case
print("lastname".islower())
print("Lastname".islower())

# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case

# join()	Converts the elements of an iterable into a string
# list => all elements of the list must be string
print("|".join(["welcome", "to", "the", "program"]))
print(" ".join(["welcome", "to", "the", "program"]))
# TypeError: sequence item 0: expected str instance, int found
# print("-".join([1, 2, 3, 4])) 
print("-ASGHAR-".join(["welcome", "to", "the", "program"]))

# ljust()	Returns a left justified version of the string
# *********************
# hello world**********
print("hello world".ljust(20,  "*"), "hello world")
print("".ljust(20,  "*"), "hello world")

# lower()	Converts a string into lower case
print("Hello world".lower())

# lstrip()	Returns a left trim version of the string
print("  Hello world    ".strip())
print("**Hello world**".strip("*")) # strip
print("**Hello world**".rstrip("*")) # right strip
print("**Hello world**".lstrip("*")) # left strip
print("**Hello world**".lstrip(" ")) # left strip
print("**    Hello world    **".lstrip(" ")) # left strip
print("**************".lstrip("*")) # 
print("**************".rstrip("*")) # 
print("**************".strip("*")) #
print("".join("welcome to the program".split()))
print("welcome-to-the-program".split("-"))
print("welcome-to-the-program".split("to"))
print("welcome*to*the*program".split("*"))

# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
print("hello world".replace("h", "m"))
print("hello world".replace("l", "asghar"))
#                        old str, new str, count
print("hello world".replace("l", "asghar", 1))
print("hello world".replace("world", "asghar"))
print("hello world".replace(" ", ""))

# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
print("hello world".upper())
# zfill()	Fills the string with a specified number of 0 values at the beginning