from time import sleep

string = "Hello world"
for i in range(1, 101):
    print(f"\r{string[0: i]}", end="")
    # print(f"\r{'*'*i}", end="")
    # print(f"\r{'█'*i}", end="")
    sleep(0.3)

# return carriage

# print("Hello hello\rmamadha")
# "mamad hello"

# print("Hello world\r")
# "Hello world"
# "MamadAsghar"
