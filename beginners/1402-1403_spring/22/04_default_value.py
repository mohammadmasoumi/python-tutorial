

def add(a, b: int = 12):
    # default b: 12
    return a + b


print(add(10))
print(add(10, 13))


def get_full_name(fname: str = "asghar", lname: str = "asghari"):
    return fname + lname


print(get_full_name())
print(get_full_name("akbar"))
print(get_full_name(lname="akbari"))
print(get_full_name("akbar", "akbari"))


# default values must be defined at the end of params
# def get_full_name(fname: str = "asghar", lname: str):
#     return fname + lname


def add_list(name, names=[]):
    print(f"names: {id(names)}")
    # names = []
    names.append(name)
    print(names)


add_list("asghar")
add_list("akbar")
add_list("soghra", [])
add_list("kobra")


def add_set(name, names=set()):
    print(f"names: {id(names)}")
    names.add(name)
    print(names)


add_set("asghar")
add_set("akbar")
add_set("soghra", set())
add_set("kobra")
