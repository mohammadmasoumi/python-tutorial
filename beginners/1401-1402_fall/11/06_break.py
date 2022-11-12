"""
my_list = []

append 2
insert 0 1
remove 1
clear
exit
pop 0 | pop
"""
my_list = []

# a, *b = 12
# a: 12, b: []

while True:
    # command, *values = ["insert", "0", "1"]
    # command, *values = "insert 0 1".split()
    # command: "insert"
    # values: ["0", "1"]

    command, *values = input().split()

    if command == "insert":
        my_list.insert(int(values[0]), values[1])

        6 = 13 // 2
        6.5 = 13 / 2