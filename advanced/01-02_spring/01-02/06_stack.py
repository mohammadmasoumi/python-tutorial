
def printer1(msg):
    print(f"[msg1]: {msg}")


def printer2(msg):
    print(f"[msg2]: {msg}")


def printer3(msg):
    print(f"[msg3]: {msg}")


def printer4(f, msg):
    # f: printer1, msg: "Hello from the otherside"
    f(msg)


def caller(f, param):
    # f: printer1, param: "Hello from the otherside" 
    # printer1( "Hello from the otherside" )
    f(param)
    printer4(f, msg)
    printer1(msg)


"""

|            |
|            |
|            |
|            |
|            |
|            |
|            |
______________
     stack

|            |
|            |
|            |
|            |
|            |
|            |
|  [caller]  |
______________
     stack

|            |
|            |
|            |
|            |
|            |
| [printer1] |
|  [caller]  |
______________
     stack

|            |
|            |
|            |
|            |
|            |
|            |
|  [caller]  |
______________
     stack

|            |
|            |
|            |
|            |
|            |
| [printer4] |
|  [caller]  |
______________
     stack

|            |
|            |
|            |
|            |
| [printer1] |
| [printer4] |
|  [caller]  |
______________
     stack

|            |
|            |
|            |
|            |
|            |
| [printer1] |
|  [caller]  |
______________
     stack

|            |
|            |
|            |
|            |
|            |
|            |
|            |
______________
     stack

LIFO (last In First Out)
"""

caller(printer1, "Hello from the otherside") # [*]


