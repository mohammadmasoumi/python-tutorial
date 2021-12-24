"""
All supported commands


append item
insert index item
extend list 
pop index
remove item
exit
sort
reverse
print
"""

# initialize my_list
my_list = []

# constants
APPEND = 'append'
EXTEND = 'extend'
EXIT = 'exit'


# flag
is_finished = False

while not is_finished:
    my_input = input().split()

    # if user enter nothing 
    if not my_input:
        continue

    command = my_input.pop(0)

    print(f"command: {command}, my_list: {my_list}, my_input: {my_input}")

    if command == APPEND:
        if len(my_input) != 1:
            print("Invalid command!")
        else:
            my_input.append(my_input[0])

    elif command == EXTEND:
        my_input.extend(my_input)

    elif command == EXIT:
        is_finished = True
  


