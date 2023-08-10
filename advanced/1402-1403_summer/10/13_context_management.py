# handle external connection

"""
context -> open and close
"""

class FileContextManager:

    def __init__(self, name, mode):
        print("initializing")
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Starting")
        self.file = open(self.name, self.mode)
        print("Opening")
        return self.file

    def __exit__(self, err_type, err_value, err_tb):
        print("Closing")
        self.file.close()
        print("Closed")

# __init__
# __start__ -> Captured what has retured via as
# __exit__ 
with FileContextManager('areyouawake.txt', 'r') as file:
    print("----------------------")
    c = 0
    for line in file.readlines():
        print(f"line{c} -> {line}")
        c += 1
    print("----------------------")