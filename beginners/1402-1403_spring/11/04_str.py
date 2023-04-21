# string
# https://www.w3schools.com/python/python_ref_string.asp

# Len ---------------------------------------------------------
string = "helloworld"
print(len(string))

# Count ------------------------------------------------------
# string.count(value, start, end)
#  Returns the number of times a specified value occurs in a string
string = "|||hello|||world|||"
print(string.count("|"))

# "d|||".count("|")
print(string[-4:].count("|"))

print(string.count("|", 4, 11))

# Replace ----------------------------------------------------
string = "|||hello|||world|||"

# immutable - re-assignment
# string = string.replace("|", "*")
print(string.replace("|", "*"))
print(string)

print(string[:-4] + string[-4:].replace("|", "*"))


# Count ----------------------------------------------------


