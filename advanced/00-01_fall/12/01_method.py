def full_name(first_name, last_name):
    print(f"{first_name}-{last_name}")


# def get_unlimited_parameters(*args):
# *args => tuple
# **kwargs => kwargs
def get_unlimited_parameters(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # dict


def get_kwrags(**kwargs):
    if kwargs.get("ali"):
        print(kwargs.get("ali"))


def get_options(a, b, **options):
    print(a + b)
    if "c" in options:
        print(a + b + options.get("c"))


full_name("Mohammad", "Masoumi")
# SyntaxError: positional argument follows keyword argument
# get_unlimited_parameters("A", "B", "C", "D", {"a": 20}, a=2, b=3, asghar=5, 20)
get_unlimited_parameters("A", "B", "C", "D", {"a": 20}, 20, a=2, b=3, asghar=5)
get_kwrags(ali=2)
get_kwrags(hassan=2)
get_options(10, 20, c=30)
get_options(10, 20, d=30)
