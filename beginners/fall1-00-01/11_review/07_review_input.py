name1 = "Hello world"
print(name1.split()) # ['Hello', 'world']

name2 = "Hello-world-Hello-world"
print(name2.split("-")) # ['Hello', 'world', 'Hello', 'world']

name3 = "He - llo - He - llo - He - llo"
print(name3.split(" - ")) # ['He ', ' llo ', ' He ', ' llo ', ' He ', ' llo']


name4 = "He-llo-He-llo-He-llo"
print(name4.split("-")) # ['He', 'llo', 'He', 'llo', 'He', 'llo']

#
print("-------------------------------------------")
#b = input()

c = "[1, 2, 3, 4, 5]"
# ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']
print(list(c))

#print(f"b: {b}, type: {type(b)}")

#a = input().split()
#print(f"a: {a}")