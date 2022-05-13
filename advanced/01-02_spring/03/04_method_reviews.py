
def unlimited_positional_args(*args):
    print(f"args: {args}")

unlimited_positional_args(1, 2, 3, 4)
unlimited_positional_args("a", "b", "c")


def unlimited_key_value_args(**kwargs):
    print(f"kwargs: {kwargs}")

unlimited_key_value_args(first_name="ali", last_name="alavi", city="varamin")
unlimited_key_value_args(a=10, b=11, c=12)


def unlimited_positional_args_and_key_value_args(*args, **kwargs):
    print(f"args: {args}, kwargs: {kwargs}")

unlimited_positional_args_and_key_value_args(12, 13, first_name="ali", last_name="alavi")
