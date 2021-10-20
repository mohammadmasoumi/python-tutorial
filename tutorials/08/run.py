"""
1. the name of the top-level environment of the program, which can be checked using
    the __name__ == '__main__' expression; and

2. the __main__.py file in Python packages.
"""

# When a Python module or package is imported, __name__ is set to the module’s name.
# Usually, this is the name of the Python file itself without the .py extension
import main_package
import configparser
from concurrent.futures import process

print(process.__name__)
print(configparser.__name__)

if __name__ == '__main__':
    # from main_package.sub_package_01.run import runner_from_sub_package
    # from main_package.run import runner_from_main_package
    #
    # print(f"runner_from_sub_package.__name__: {runner_from_sub_package.__name__}")
    # print(f"runner_from_main_package.__name__: {runner_from_main_package.__name__}")
    pass