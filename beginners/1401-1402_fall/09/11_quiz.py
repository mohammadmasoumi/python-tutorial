#       012345678910 ... 
word = "hello hello hello hello"
start_index = 0
counter = 0

for _ in range(len(word)):
    # start_index: 0
    # start_index: 5
    # start_index: 11
    # start_index: 17
    position = word.find("hello", start_index)
    # position: 0
    # position: 6
    # position: 12
    # position: -1

    if position == -1:
        break

    start_index = position + len("hello")

    counter += 1
    print(position)

    if counter == 2:
        break