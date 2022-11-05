# ljust()	Returns a left justified version of the string
# "        hello world           ********************"
print("        hello world           ".ljust(50, "*"))

print("hello world".ljust(50, " "))
print("hello world".rjust(50, " "))
print("hello world".center(50, " "))

# replace()	Returns a string where a specified value is replaced with a specified value
print("hello world hello hello".replace("h", "H"))
print("hello world hello hello".replace("h", "H", 2))

# -------------------------------
word = "hello world hello hello"
word.replace("h", "H")
word = word.replace("h", "H")
print(f"word: {word}")


# zfill()	Fills the string with a specified number of 0 values at the beginning
print("hello world".zfill(20))
print("1".zfill(3))
print("111".zfill(3))
