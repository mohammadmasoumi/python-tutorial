# helloworld

#         0123456789
string = "helloworld"

# __getitem__
print(string[0])

# concatenation
string = "hello" "world"
print(string)

string = "hello"
"world"

string = (
    "hello"
    "world"
)
print(string)

# negative index 
# positive index
# slicing range index {start:end(not included):step}
print(string[0:5]) # substring
print(string)

"""
(method) def count(
    x: str,
    __start: SupportsIndex | None = ...,
    __end: SupportsIndex | None = ...
) -> int
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end]. Optional arguments start and end are interpreted as in slice notation.
"""
print("helloworld".count("o"))
print("helloworld".count("o", 13, 10))

# capitalize()	Converts the first character to upper case
print("helloworld".capitalize())
print("hello world".capitalize())
print("Helloworld".capitalize())

# 
print("hello world".title())
print("helloworld".title())
print("helloworld".title())

# casefold()	Converts string into lower case
# Return a version of the string suitable for caseless comparisons.
print("HellO World".casefold())

# center()	Returns a centered string
print("hello".center(30))
print("abc".center(10))

# endswith()	Returns true if the string ends with the specified value
print("helloworld".endswith("world"))
print("helloworld".endswith("d"))
print("helloworld".endswith("o", 0, 5))
print("helloworld".endswith("w", 0, 5))

# startwith()
print("helloworld".startswith("hello"))
print("helloworld".startswith("hello", 2, 10))

# expandtabs()	Sets the tab size of the string
print("hello\tworld".expandtabs(16))


# find()	Searches the string for a specified value and returns the position of where it was found
print("helloworld".find("ll", 2, 10)) # return start index
print("helloworlld".find("ll", 2, 20)) # left find
# such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
print("helloworlld".rfind("ll", 2, 20)) 


PATTERN = "hello {name} world"

# format()	Formats specified values in a string
print("hello {name} world".format(name="asghar")) # keyword args
print("hello {name} world {lastname}".format(lastname="asghari", name="asghar")) # keyword args
print("hello {} world {}".format("asghari", "asghar")) # positional args
print("hello {1} world {0}".format("asghari", "asghar")) # index args

name = "asghar"
print(f"hello {name} world")

print(PATTERN.format(name="asghar"))
print(PATTERN.format(name="hassan"))

name = "asghar"
print(f"hello {name} world")

name = "hassan"
print(f"hello {name} world")


# index()	Searches the string for a specified value and returns the position of where it was found
print("helloworld".find("ll", 2, 10))
print("helloworld".find("oo", 2, 10)) # -1 doesn't exist
print("helloworlld".index("ll", 2, 10))

# Traceback (most recent call last):
#   File "c:\Users\MFT SERVER\Desktop\Python\python-beginner-winter1401\12\01_string_methods.py", line 106, in <module>
#     print("helloworlld".index("oo", 2, 10))
# ValueError: substring not found
# print("helloworlld".index("oo", 2, 10)) 

# isalnum()	Returns True if all characters in the string are alphanumeric
# alphanumeric = alphabetic + numeric
print("all1234".isalnum())
print("all1234@".isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
print("all1234#".isalpha())
print("1234".isalpha())

isalpha = True 
for char in "abc":
    if not ((ord("a") <= ord(char) <= ord("z")) or (ord("A") <= ord(char) <= ord("Z"))):
        isalpha = False
        break

print(isalpha)

isnum = True 
for char in "1234":
    if not (ord("0") <= ord(char) <= ord("9")):
        isnum = False
        break

print(isnum)

print(ord("😀"))
print(ord("👿"))


# https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth
# isdecimal() ⊆ isdigit() ⊆ isnumeric()
# +-------------+-----------+-------------+----------------------------------+
# | isdecimal() | isdigit() | isnumeric() |          Example                 |
# +-------------+-----------+-------------+----------------------------------+
# |    True     |    True   |    True     | "038", "੦੩੮", "０３８"           |
# |  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"             |
# |  False      |  False    |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"  |
# |  False      |  False    |  False      | "abc", "38.0", "-38"             |
# +-------------+-----------+-------------+----------------------------------+

# "0123456789"  DIGIT ZERO~NINE
# "٠١٢٣٤٥٦٧٨٩"  ARABIC-INDIC DIGIT ZERO~NINE
# "०१२३४५६७८९"  DEVANAGARI DIGIT ZERO~NINE
# "০১২৩৪৫৬৭৮৯"  BENGALI DIGIT ZERO~NINE
# "੦੧੨੩੪੫੬੭੮੯"  GURMUKHI DIGIT ZERO~NINE
# "૦૧૨૩૪૫૬૭૮૯"  GUJARATI DIGIT ZERO~NINE
# "୦୧୨୩୪୫୬୭୮୯"  ORIYA DIGIT ZERO~NINE
# "௦௧௨௩௪௫௬௭௮௯"  TAMIL DIGIT ZERO~NINE
# "౦౧౨౩౪౫౬౭౮౯"  TELUGU DIGIT ZERO~NINE
# "೦೧೨೩೪೫೬೭೮೯"  KANNADA DIGIT ZERO~NINE
# "൦൧൨൩൪൫൬൭൮൯"  MALAYALAM DIGIT ZERO~NINE
# "๐๑๒๓๔๕๖๗๘๙"  THAI DIGIT ZERO~NINE
# "໐໑໒໓໔໕໖໗໘໙"  LAO DIGIT ZERO~NINE
# "༠༡༢༣༤༥༦༧༨༩"  TIBETAN DIGIT ZERO~NINE
# "၀၁၂၃၄၅၆၇၈၉"  MYANMAR DIGIT ZERO~NINE
# "០១២៣៤៥៦៧៨៩"  KHMER DIGIT ZERO~NINE
# "０１２３４５６７８９"  FULLWIDTH DIGIT ZERO~NINE
# "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"  MATHEMATICAL BOLD DIGIT ZERO~NINE
# "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"  MATHEMATICAL DOUBLE-STRUCK DIGIT ZERO~NINE
# "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"  MATHEMATICAL SANS-SERIF DIGIT ZERO~NINE
# "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"  MATHEMATICAL SANS-SERIF BOLD DIGIT ZERO~NINE
# "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"  MATHEMATICAL MONOSPACE DIGIT ZERO~NINE

# isidentifier()	Returns True if the string is an identifier
# keyword + identifier
print("def".isidentifier())
print("asghar".isidentifier())
print("#asghar".isidentifier())
print("class".isidentifier())
print("name-last".isidentifier())


# islower()	Returns True if all characters in the string are lower case
print("Lower".islower())
print("lower".islower())
print("loWer".islower())
print("LOWER".islower())

# isspace()	Returns True if all characters in the string are whitespaces
print("   ".isspace())

# istitle()	Returns True if the string follows the rules of a title
print("The Great Gatsby".istitle())
print("The Great gatsby".istitle())

# isupper()	Returns True if all characters in the string are upper case

# join()	Joins the elements of an iterable to the end of the string
print("|".join(["the", "hello","world"]))
print(",".join(["the", "hello","world"]))
print("-".join(["the", "hello","world"]))
# TypeError: sequence item 0: expected str instance, int found
# print("-".join([1, 2, 3, 4]))
print("".join(["the", "hello","world"]))
# the|hello|world"

# lower()	Converts a string into lower case
print("HELLO".lower())
print("hello".upper())

# ljust()	Returns a left justified version of the string

print("Hello world".ljust(20, "*"), "asghar")


txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.") # sep: " "

print(len("banana               "))