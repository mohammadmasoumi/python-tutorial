# 
name = "Helloooooooooo"

"""

key value
{
    "H": 1, 
    "e": 1,
    '''
}
if I've seen letter, ++count
else {letter: 1} 
"""

#            value of H, otherwise default_value
#              key, default_value
# key: "H", value: 10 
# data["H"] = 10

# data = {}
# letter = "H"
# print(data.get(letter, 0))
# print(data)
# data[letter] = data.get(letter, 0) + 1
# letter = "a"
# data[letter] = data.get(letter, 0) + 1
# print(data)


letter_count = {}

# no case sensitive
for letter in "Hellooooooooooh":
    letter = letter.lower()
    # update
    letter_count[letter] = letter_count.get(letter, 0) + 1

# case sensitive
# for letter in "Hellooooooooooh":
#     letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)