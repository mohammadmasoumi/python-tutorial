# context manager

"""
with 

"""
# open: Context Manager

with open("asghar.txt", "w") as file:
    
    # code block
    # initialize
    # enter
    # exit

    file.write("Hello")


class FileContextManager:

    def __init__(self, file_name, mode):
        print("__init__")
        self._file_name = file_name
        self._mode = mode
        self._file = None

    def __enter__(self):
        print("__enter__")
        self._file = open(self._file_name, self._mode)

        return self._file

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("__exit__")

        self._file.close()


with FileContextManager("asghar2.txt", "a") as f:
    
    f.write("Hello")