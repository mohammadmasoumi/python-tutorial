import sys


class RedirectOutput:

    def __init__(self):
        self.prev_stdout = sys.stdout
        self.next_stdout = None

    def __enter__(self):
        file = open('out2.txt', 'w')
        sys.stdout = file
        self.next_stdout = file

    def __exit__(self, err_type, err_value, err_tb):
        sys.stdout = self.prev_stdout
        self.next_stdout.close()


with RedirectOutput():
    print("Hello")

print("Bye")
