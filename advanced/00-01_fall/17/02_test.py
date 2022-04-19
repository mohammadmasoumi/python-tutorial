# from game import Engine
#
# print(__name__)
# engine = Engine()
# engine.run()

# import sys
#
# sys.stdout.write("-------------\n")
# sys.stdout.write("-------------\n")
# # sys.stdout.flush()
# sys.stderr.write("\x1b[2J\x1b[H")
# sys.stdout.write("-------------\n")


# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# print out some text
print('hello geeks\n' * 10)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()