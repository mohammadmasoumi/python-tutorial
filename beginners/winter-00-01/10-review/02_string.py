# string - immutable

name1 = "ali"
name2 = "asghar"

# concatenation
name3 = name1 + name2

# re-assignment
name4 = "asghar"
name4 += "ali"
print(name4)

print(name1 + name2)
print("ali" "asghar")
print((
    "ali"
    "asghar"
))

#  len
print(len(name3))

# range index

# positive index
# negative index
# -3-2-1
#  012
# "ali"

# شامل ایندکس پایانی نمیشود.
#        start:end(not included):step
# aliasghar
# -5 -4 -3 -2 -1
#  0  1  2  3  4
print(name3[1:2])
print(name3[-8:2])
print(name3[-1: :-1])
print(name3[-1: :-2])

# method

# .split() default=" " space
print("Hello How are you?".split())
print("Hello*How*are*you?".split("*"))

# .join(iterable) ["Hello", "How", "are", "you"]
# iterable -> each element must be string
print(" ".join(["Hello", "How", "are", "you"]))
# TypeError: sequence item 3: expected str instance, int found
# print(" ".join(["Hello", "How", "are", 1]))
print(" | ".join(["Hello", "How", "are", "you"]))

# strip
print("  Mobin   ".strip())
print("  Mobin   ".lstrip())
print("  Mobin   ".rstrip()) 
print("**  Mobin  **".strip("*"))

# find
#                substring, start, end
# S.find(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found,
# such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
# Return -1 on failure.
print("Hello How are you mobin?".find("H"))
print("Hello How are you mobin?".find("H", 1))
print("Hello How are you mobin?".find("o", 5, 10))

# startwith/endswith
print("helloHowAreYou".startswith("hello"))
print("helloHowAreYou".endswith("You"))

# center
# کلش 20 تا است
print("Mobin".center(20))
print("Mobin".center(20, "-"))

# count
print("mohammad".count("mo"))
print("mohammad".count("m"))


# index
# S.index(sub[, start[, end]]) -> int

# Return the lowest index in S where substring sub is found,
# such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

# Raises ValueError when the substring is not found.
# ValueError: substring not found
# print("aliasgharaliasghar".index("ali", 1, 2))
print("aliasgharaliasghar".index("ali", 1, 20))

# islower, isupper, lower, upper
print("Hello".islower())
print("Hello".isupper())
print("Hello".lower())
print("Hello".upper())


# for loop
for character in name3:
    print(character)

