word = "hello world"
new_word = ""

for index, item in enumerate(word):
    # new_word += item if index == len(word) - 1 else item + "*" 
    if index == len(word) - 1:
        new_word += item 
    else:
        new_word += item + "*" 

    print(f"new_word: {new_word}")

# "h*e*l*l*o* *w*o*r*l*d"
print(new_word)