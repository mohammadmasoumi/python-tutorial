# callme

# variable callme1
def callme1(f):
    # f = say_hello
    f()

# variable say_hello 
def say_hello():
    print("Hello")

"""
First In Last Out
Last In First Out

|         |
|say_hello|
| callme1 |
|   main  |
__________

|         |
|         |
| callme1 |
|   main  |
__________

|         |
|         |
|         |
|   main  |
__________

  STACK
"""

callme1(say_hello)