word = "     hello    world       "

start_index1 = word.index("h")
start_index2 = word.index("d")

words = word.split(" ")
# ["hello", "word"]
#
#     "           "      + "helloword"    + "          "
print(" " * start_index1 + "".join(words) + " " * (len(word) - start_index2))

print(word.replace(" ", ""))
print(word[start_index1: start_index2].replace(" ", "*").split("*"))
print(word[start_index1: start_index2].replace(" ", "*").split("*"))
print(word[:word.index("o")+1] + word[word.index("w"):])