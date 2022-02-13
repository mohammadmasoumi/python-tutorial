
def is_palindram(string):
    return string[: len(string)//2] == string[len(string)//2 + 1:]


print(is_palindram("aba"))
print(is_palindram("ab"))
