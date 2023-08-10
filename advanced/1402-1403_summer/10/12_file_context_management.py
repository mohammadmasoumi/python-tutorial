# Context management

# with

# file = open('areyouawake.txt', 'w')
with open('areyouawake.txt', 'w') as file: # -- start context
    # open file
    file.write('Yes, we are awake!')

    # -- end context
    # close file


