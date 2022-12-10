# class str:
#     pass

# class int:
#     pass

class Mouse:

    def __init__(self, name):
        self.name = name

    def __int__(self):
        return 10

    def __str__(self):
        return f"--{self.name}--"


# name = input()
jerry = Mouse("jerry")
# jerry = Mouse(input())

# print(f"{str(jerry)}")
# print(str(jerry))
print(int(jerry))

stringify_jerry = str(jerry)
print(stringify_jerry)
