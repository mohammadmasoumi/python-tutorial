# map
my_list = [1, 2, 3, 4]
print(map(lambda x: x * 2, my_list))
print(list(map(lambda x: x * 2, my_list)))
print(set(map(lambda x: x * 2, my_list)))
print(tuple(map(lambda x: x * 2, my_list)))

sentence = "Hello this Is a Sentence"
print(sentence.title())
# print(sentence.capitalize())

print(sentence.split())
print(list(map(lambda x: x.capitalize(), sentence.split())))
print("|".join(map(lambda x: x.capitalize(), sentence.split())))
