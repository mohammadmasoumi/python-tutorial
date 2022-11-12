from time import sleep

print("hello\nworld")
print("hello\tworld")
print("hello\tworld".expandtabs(20))
print("hello\bworld")  # backspace


print("hello\rworld")  # return carriage
# hello
# world
# helloooooo
# worldooooo
print("hello\r")
print("\rhello")
print("hell\rworld")  # return carriage
print("hellooooooo\rworld")  # return carriage


# string = "Hello world"
# for i in range(1, 101):
#     print(f"\r{string[0: i]}", end="")
#     # print(f"\r{'*'*i}", end="")
#     # print(f"\r{'█'*i}", end="")
#     sleep(0.3)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# string = "How are you?"
# for i in range(1, 20):
#     print(f"\r{string[0: i]}", end="")
#     # print(f"\r{'*'*i}", end="")
#     # print(f"\r{'█'*i}", end="")
#     sleep(0.1)


print("------------------")
for i in range(1, 101):
    # print(f"\r{'█'*i}", end="")
    print(f"\r{bcolors.FAIL}{'☠'*i}", end="")
    # print(f"\r{'⚠'*i}", end="")
    sleep(0.3)
