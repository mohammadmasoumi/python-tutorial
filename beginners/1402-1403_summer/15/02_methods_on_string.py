# Method on string
# https://www.w3schools.com/python/python_strings_methods.asp

#         0123456789
string = "helloworld"

# concatenation
string = "hello"     "world"
print(string)

string = "hello"
"world"
print(string)

string = (
    "hello"
    "world"
)
print(string)

# tuple
string = "hello",
"world"
print(string)

# negative index
# positive index
# slicing {start:end(not included):step}
print(string[0:5])  # substring
print(string)

# Count
"""
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end]. Optional arguments start and end are interpreted as in slice notation.
"""
print("helloworld".count("o"))
print("helloworld".count("o", 13, 10))
print("thathathat".count("that"))

# capitalize()	Converts the first character to upper case
"""
Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest.lower case.
"""
print("helloworld".capitalize())
print("hello world".capitalize())
print("Helloworld".capitalize())

# title()
"""
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have.lower case.
"""
print("helloworld".title())
print("hello world".title())
print("Helloworld".title())

# upper()
"""
Return a copy of the string converted to uppercase.
"""
print("helloworld".upper())
print("hello world".upper())
print("Helloworld".upper())

# .lower()
"""
Return a copy of the string converted to lowercase.
"""
# ctrl + shift + l
print("helloworld".lower())
print("hello world".lower())
print("Helloworld".lower())

# casefold()	Converts string into lower case
# Return a version of the string suitable for caseless comparisons.
"""
It is similar to the lower() method, but the casefold() method converts more characters into lower case. For example, the German lowercase letter 'ß' is equivalent to 'ss' . Since it is already lowercase, the lower() method would not convert it; whereas the casefold() converts it to 'ss' .
"""
print("HellO World".casefold())

# center()	Returns a centered string
"""
Return a centered string of length width.

Padding is done using the specified fill character (default is a space).
"""
print("hello".center(30))
print("abc".center(10, "%"))

# endswith()	Returns true if the string ends with the specified value
"""
(method) endswith(__suffix: str | tuple[str, ...], __start: SupportsIndex | None = ..., __end: SupportsIndex | None = ..., /) -> bool
"""
print("helloworld".endswith("world"))
print("helloworld".endswith("d"))
#  012345
# "helloworld"[0:5] => "hello"
print("helloworld".endswith("o", 0, 5))
print("helloworld".endswith("w", 0, 6))

# startswith()
"""
S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.
"""
print("helloworld".startswith("hello"))
print("helloworld".startswith("h"))
print("helloworld".startswith("hello", 2, 10))
print("helloworld".startswith("hello", 0, 10))
print("helloworld".startswith("hello", 0, 2))

# find()	Searches the string for a specified value and returns the position of where it was found
"""
S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.
"""
#      0123456789
print("helloworld".find("ll", 2, 10))  # return start index
# "helloworlld"[2:20] => "lloworlld"
print("helloworlld".find("ll", 2, 20))  # left find
# such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
print("helloworlld".find("ll", 3, 6))  # -1
# left find
#       ->
# start                  end
# --------------------------
# right find
#                      <-
# start                  end
"""
S.rfind(sub[, start[, end]]) -> int

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.
"""
#      012345678910
print("helloworlld".rfind("ll", 2, 20))
print("helloworlad".rfind("la", 2, 20))

print("helloworlad".rfind("la", -6, -1))

# string = "helloworld"
# # string = input()
# if string.find("ll", 2, 10) == 2:
#     print("Bingo")

PATTERN = "hello {name} world"
DATABASE_CONNECTION = "postgres://{username}:{password}@{host}:{port}/{database}"

# format()	Formats specified values in a string
print("hello {name} world".format(name="asghar"))  # keyword args
print(DATABASE_CONNECTION.format(username='asghar', password='1234',
      host='localhost', port='5432', database='asghar-db'))
print("hello {name} world {lastname}".format(
    lastname="asghari", name="asghar"))  # keyword args
print("hello {} world {}".format("asghari", "asghar"))  # positional args
print("hello {1} world {0}".format("asghari", "asghar"))  # index args

# index()	Searches the string for a specified value and returns the position of where it was found
"""
S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
"""
print("helloworld".find("ll", 2, 10))
print("helloworld".find("oo", 2, 10))  # -1 doesn't exist
print("helloworlld".index("ll", 2, 10))
# print("helloworld".index("ll", 5, 10)) # ValueError: substring not found

print("↉⅛⅘".isdecimal())
print("↉⅛⅘".isdigit())
print("↉⅛⅘".isnumeric())

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

# isalnum()	Returns True if all characters in the string are alphanumeric
# alphanumeric = alphabetic + numeric
"""
Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.
"""
print("all1234".isalnum())
print("all1234@".isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
print("all1234#".isalpha())
print("1234".isalpha())
print("asghar".isalpha())

# isidentifier()	Returns True if the string is an identifier
# keyword + identifier
"""
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as "def" or "class".
"""
# keyword + valid variable name
print("def".isidentifier())
print("asghar".isidentifier())
print("name_last".isidentifier())
print("#asghar".isidentifier())
print("class".isidentifier())
print("name-last".isidentifier())
print("Asghar".isidentifier())
print("name last".isidentifier())
print("ASghar".isidentifier())
print("ASGHAR".isidentifier())
print("ASGH@R".isidentifier())
print("1asghar".isidentifier())
print("asghar1".isidentifier())
ASGHAR = 12
# name-last = 12

# method_name = input()

# exec(f"""
# def {method_name}(name):
#     print('hello', name)

# {method_name}('asghar')
# """)
# eval('khafan_function("akbar")')

# islower()	Returns True if all characters in the string are lower case
print("Lower".islower())
print("lower".islower())
print("loWer".islower())
print("LOWER".islower())

# isupper()	Returns True if all characters in the string are upper case
print("Lower".isupper())
print("lower".isupper())
print("loWer".isupper())
print("LOWER".isupper())

# isspace()	Returns True if all characters in the string are whitespaces
print("   ".isspace())
print(" a  ".isspace())

# istitle()	Returns True if the string follows the rules of a title
print("The Great Gatsby".istitle())
print("The Great gatsby".istitle())


# join()	Joins the elements of an iterable to the end of the string
print("|".join(["the", "hello", "world"]))
print(",".join(["the", "hello", "world"]))
print("-".join(["the", "hello", "world"]))
# TypeError: sequence item 0: expected str instance, int found
# print("-".join([1, 2, 3, 4]))
print("".join(["the", "hello", "world"]))
# the|hello|world"

# lower()	Converts a string into lower case
print("HELLO".lower())
print("hello".upper())

# ljust()	Returns a left justified version of the string

"""
|            | 
|            |
"""
print("Hello world".rjust(20), "asghar")
print("Hello".rjust(20), "asghar")
print("World".rjust(20), "asghar")
print("Hello world".ljust(20), "asghar")
print("Hello world".ljust(20, "*"), "asghar")


# txt = "banana"
# x = txt.ljust(20)
# print(x, "is my favorite fruit.") # sep: " "
# print(len("banana               "))

# zip
# my_scores = [1, 2, 3, 4]
# my_names = ["mi`ad", "abolfazl", "Mr Semnani"]
# my_ages = [14, 16, "?"]

# print(list(zip(my_names, my_scores, my_ages)))

"""
Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.
"""

txt = "Good night Sam!"
x = "mSa"  # m -> e | a -> o
y = "eJo"  # S -> J |
z = "odnght"  # remove
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))
# "Good night Sam!"
# "G i Joe!"

txt = "Hello world asghar"
x = "sh"
y = "kb"
z = "g"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))


# strip()
"""
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.
"""
print("   hello world    ".strip())  # default: space
print("--   hello-world   --".strip("-"))
print("--   hello-world   --".strip("-").strip())
print("--   hello-world   --".rstrip())
print("--   hello-world   --".rstrip('--'))
print("--   hello-world   --".lstrip('--'))
print("--   hello-world   --".strip('--'))

#
"""
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done.
"""
txt = "50"
x = txt.zfill(10)
print(x)

# replace
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# expandtabs()
print("hello\tworld")
print("hello\tworld".expandtabs(10))

# partition
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)  # ('I could eat ', 'bananas', ' all day')

txt = "I could eat bananas all day bananas"
x = txt.partition("bananas")
print(x)  # ('I could eat ', 'bananas', ' all day')
