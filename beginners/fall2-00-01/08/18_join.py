# list of str
"".join(["a", "b"])
# "".join([1, 2]) # TypeError: sequence item 0: expected str instance, int found


"""
input: a list, join_with
out: str
"""


def my_join(a_list, join_with):
    acc = ""

    for item in a_list:
        acc += item + join_with

    return acc[:-1]


item = my_join(["a", "b"], "*")
print(item)
