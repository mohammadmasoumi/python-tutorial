"""
1 2 3 4 5
5 1 2 3 4
4 5 1 2 3
3 4 5 1 2
2 3 4 5 1
1 2 3 4 5
5 1 2 3 4

6 % 5
"""
from malware import malware_decorator


@malware_decorator
def login(username, password):
    pass


login("asghar", "1234")
login("hamid", "12345")
