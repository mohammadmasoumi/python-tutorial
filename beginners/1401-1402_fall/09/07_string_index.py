#       012345678910
word = "hello world"

# 1.
# default: " "
# word.split() = ["hello", "world"]
# ["hello", "world"][0]
print(word.split()[0])

# 2.
print(word[-1])
print(word[:5])

# 3.
s = ""
for item in word:
    if item == " ":
        break

    s += item

print(s)

# 4.
s = ""
started = False
for item in word:
    if started:
        s += item

    if item == " ":
        started = True

print(s)

# 
# word = "hello world"
word = "hello world"
new_word = ""

for index, item in enumerate(word):
    # new_word += item if index == len(word) - 1 else item + "*" 
    if index == len(word) - 1:
        new_word += item 
    else:
        new_word += item + "*" 

# "h*e*l*l*o* *w*o*r*l*d"
print(new_word)

new_word = ""
for index, item in enumerate(word):
    # new_word += item if index == len(word) - 1 else item + "*" 
    new_word += item + "*" 

print(new_word[:-1])