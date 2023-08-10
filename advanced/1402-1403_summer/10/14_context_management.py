# handle external connection

"""
context -> open and close
"""


class FileContextManager:

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, err_type, err_value, err_tb):
        print(
            f"err_type: {err_type}, err_value: {err_value}, err_tb: {err_tb}")

        self.file.close()

        if isinstance(err_value, ValueError):
            print("Valuuuuuuuuuuuuuuuuue error")
            return True

        # suppressed: forcibly put an end to
        # If we returned True here, any exception would be suppressed!
        return False


with FileContextManager('areyouawake.txt', 'r') as file:
    print("----------------------")
    c = 0
    for line in file.readlines():
        print(f"line{c} -> {line}")
        c += 1

    raise ValueError('This is a dummy value exception!')
    print("----------------------")
